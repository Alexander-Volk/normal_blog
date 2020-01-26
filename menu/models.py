from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.sites.models import Site
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from django.conf import settings


class Menu(models.Model):
    name = models.CharField('Название', max_length=50)
    status = models.BooleanField('Только для зарегестрированных', default=False)
    published = models.BooleanField('Отображать?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(MPTTModel):
    title = models.CharField('Название пункта меню на сайте', max_length=50)
    name = models.CharField('Название латиницей', max_length=50)
    parent = TreeForeignKey(
        'self',
        verbose_name='Родительский пунк',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey('Menu', verbose_name='Меню', on_delete=models.CASCADE)
    status = models.BooleanField('Только для зарегестрированных', default=False)
    url = models.CharField('Ссылка на внешний ресурс', max_length=100, null=True, blank=True)
    anchor = models.CharField('Якорь', max_length=50, null=True, blank=True)
    content_type = models.ForeignKey(
        ContentType,
        verbose_name='Ссылка на',
        limit_choices_to=settings.MENU_APPS,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(verbose_name='Id записи', default=1, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    sort = models.PositiveIntegerField('Порядок', default=0)
    published = models.BooleanField('Отображать?', default=True)

    def get_anchor(self):
        if self.anchor:
            return f'{Site.objects.get_current().domain}/#{self.anchor}'
        return False

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    class MPTTMeta:
        order_insertion_by = ['sort']