from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg


class Sight(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='sight_images')

    def average_rating(self):
        avg_rating = self.rating_set.aggregate(average=Avg('score'))['average']
        return avg_rating if avg_rating is not None else 0

    @staticmethod
    def top_rated_sights(limit=4):
        return Sight.objects.annotate(avg_rating=Avg('rating__score')).order_by('-avg_rating')[:limit]

class Rating(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        unique_together = ('sight', 'user')


class Comment(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserNote(models.Model):
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('sight', 'user')

