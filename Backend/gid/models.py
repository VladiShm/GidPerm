from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Sight(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='sight_images', verbose_name='Изображение')

    def average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            return ratings.aggregate(Avg('score'))['score__avg']
        return 0.0

    @staticmethod
    def top_rated_sights(limit=4):
        return Sight.objects.annotate(avg_rating=Avg('rating__score')).order_by('-avg_rating')[:limit]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'




class Comment(models.Model):
    sight = models.ForeignKey('Sight', on_delete=models.CASCADE, verbose_name='Достопримечательность')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='comment_images', null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



class UserNote(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, verbose_name='Достопримечательность')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Заметка пользователя'
        verbose_name_plural = 'Заметки пользователей'
        unique_together = ('sight', 'user')


class Visit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'sight')


class Rating(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, verbose_name='Достопримечательность')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    score = models.PositiveIntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        unique_together = ('sight', 'user')