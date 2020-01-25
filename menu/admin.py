from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'published')
    list_filter = ('published',)


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    list_display = ('title', 'name', 'parent', 'menu', 'sort', 'published')
    list_filter = ('menu', 'parent', 'published')
    search_fields = ('name', 'parent__name', 'menu__name')
    save_as = True
    list_editable = ('published',)
    mptt_level_indent = 20
