from time import time

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Category(MPTTModel):
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('url', max_length=50, unique=True)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительская категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    class Meta:
        verbose_name = 'Категория нововстей'
        verbose_name_plural = 'Категории новостей'


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50, db_index=True)
    slug = models.SlugField('url', max_length=50, unique=True, blank=True)
    body = models.TextField('Тело', blank=True, db_index=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def get_absolute_url(self):
        return reverse('blog:post_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog:post_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog:post_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Tag(models.Model):
    title = models.CharField('Тег', max_length=50)
    slug = models.SlugField('url', max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('blog:tag_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog:tag_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('blog:tag_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(models.Model):
    text = models.TextField('Комментарий')
    create_date = models.DateTimeField('Дата создания', auto_now=True)
    moderation = models.BooleanField(default=True)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )

    class Meta:
        # ordering = ['-created_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
