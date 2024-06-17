from django.contrib import admin
from .models import Sight, Rating, Comment, UserNote, Event


@admin.register(Sight)
class SightAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'average_rating')
    readonly_fields = ('average_rating',)
    verbose_name = 'Достопримечательность'
    verbose_name_plural = 'Достопримечательности'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('sight', 'user', 'score')
    verbose_name = 'Рейтинг'
    verbose_name_plural = 'Рейтинги'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('sight', 'user', 'text', 'created_at')
    readonly_fields = ('created_at',)
    verbose_name = 'Комментарий'
    verbose_name_plural = 'Комментарии'

@admin.register(UserNote)
class UserNoteAdmin(admin.ModelAdmin):
    list_display = ('sight', 'user', 'text', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    verbose_name = 'Заметка пользователя'
    verbose_name_plural = 'Заметки пользователей'

admin.site.register(Event)