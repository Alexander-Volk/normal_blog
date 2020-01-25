from django.contrib import admin

from pages.admin import ActionPublish
from .models import Post, Tag, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    extra = 1


class PostAdmin(ActionPublish):
    list_display = ('title', 'slug', 'published', 'viewed')
    list_filter = ('published',)
    list_editable = ('published',)
    search_fields = ('title', 'body',)
    save_on_top = True
    inlines = [CommentsInline]
    actions = ['unpublish', 'publish']
    filter_horizontal = ('tags',)
    fieldsets = (
        ('О посте', {
            'fields': ('author', 'title', 'slug'),
        }),
        ('Контент', {
            'fields': ('body', 'image'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags',),
        }),
        ('Настройки', {
            'classes': ('collapse',),
            'fields': ('published', 'viewed')
        })
    )


class TagAdmin(ActionPublish):
    list_display = ('title', 'slug', 'published')
    list_filter = ('published',)
    list_editable = ('published',)
    search_fields = ('title',)
    actions = ['unpublish', 'publish']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'post', 'moderation')
    list_filter = ('author', 'post')


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = 'Normal blog'
admin.site.site_header = 'Normal blog'
