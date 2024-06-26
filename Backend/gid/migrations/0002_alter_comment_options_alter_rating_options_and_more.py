# Generated by Django 5.0.6 on 2024-06-17 11:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gid', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='rating',
            options={'verbose_name': 'Рейтинг', 'verbose_name_plural': 'Рейтинги'},
        ),
        migrations.AlterModelOptions(
            name='sight',
            options={'verbose_name': 'Достопримечательность', 'verbose_name_plural': 'Достопримечательности'},
        ),
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='comment_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gid.sight', verbose_name='Достопримечательность'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='score',
            field=models.PositiveIntegerField(verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='sight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gid.sight', verbose_name='Достопримечательность'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='image',
            field=models.ImageField(upload_to='sight_images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='sight',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='UserNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gid.sight', verbose_name='Достопримечательность')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заметка пользователя',
                'verbose_name_plural': 'Заметки пользователей',
                'unique_together': {('sight', 'user')},
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_at', models.DateTimeField(auto_now_add=True)),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gid.sight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'sight')},
            },
        ),
    ]
