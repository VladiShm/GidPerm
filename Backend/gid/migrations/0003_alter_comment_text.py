# Generated by Django 5.0.6 on 2024-06-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gid', '0002_alter_comment_options_alter_rating_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
    ]
