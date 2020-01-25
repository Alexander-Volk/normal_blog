from django.db import models

from django.urls import get_script_prefix
from django.utils.encoding import iri_to_uri


class Page(models.Model):
    title = models.CharField('Заголовок', max_length=50)
    sub_title = models.CharField('Подзаголовок', max_length=25, blank=True, null=True)
    text = models.TextField('Текст', blank=True, null=True)
    edit_date = models.DateTimeField(
        'Дата редактирования',
        auto_now=True,
        blank=True,
        null=True
    )
    published_date = models.DateTimeField('Дата публикации', blank=True, null=True)
    published = models.BooleanField('Опубликовать?', default=True)
    template = models.CharField('Шаблон', max_length=50, default='pages/home.html')
    registration_required = models.BooleanField(
        'Требуется регистрация',
        help_text='Если флажок установлен, только зарегистрированные пользователи могут '
                  'просматривать страницу.',
        default=False
    )
    slug = models.CharField('url', max_length=50, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = '/'
        if not self.slug.startswith('/'):
            self.slug = '/' + self.slug
        if not self.slug.endswith('/'):
            self.slug += '/'
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return iri_to_uri(get_script_prefix().rstrip('/') + self.slug)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
