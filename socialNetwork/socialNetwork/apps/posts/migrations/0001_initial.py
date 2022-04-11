# Generated by Django 4.0.2 on 2022-04-10 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, max_length=150, verbose_name='Заголовок')),
                ('post_text', models.TextField(verbose_name='Текст поста')),
                ('post_image', models.ImageField(blank=True, upload_to='images/post/', verbose_name='Изображение поста')),
                ('post_image_url', models.ImageField(blank=True, upload_to='', verbose_name='URL изображения поста')),
                ('post_time', models.DateTimeField(verbose_name='Время создания')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_dislike', models.ManyToManyField(blank=True, related_name='post_disliked', to=settings.AUTH_USER_MODEL)),
                ('post_like', models.ManyToManyField(blank=True, related_name='post_liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.CharField(choices=[('LIKE', 'like'), ('DISLIKE', 'dislike'), (None, 'None')], default=None, max_length=7)),
                ('for_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Лайк',
                'verbose_name_plural': 'Лайки',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=350, verbose_name='Текст комментария')),
                ('comment_pubdate', models.DateTimeField(verbose_name='Дата публикации')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='posts.post')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
