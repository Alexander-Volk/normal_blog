from django.contrib import admin
from .models import Page
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ActionPublish(admin.ModelAdmin):
    def unpublish(self, request, queryset):
        rows_update = queryset.update(published=False)
        if rows_update == 1:
            message_bit = '1 story was'
        else:
            message_bit = f'{rows_update} stories were'
        self.message_user(request, f'{message_bit} successfully marked as unpublished')

    unpublish.short_description = 'Снять с публикации'
    unpublish.allowed_permissions = ('change',)

    def publish(self, request, queryset):
        rows_update = queryset.update(published=True)
        if rows_update == 1:
            message_bit = '1 story was'
        else:
            message_bit = f'{rows_update} stories was'
        self.message_user(request, f'{message_bit} successfully marked as published')

    publish.short_description = 'Опубликовать'
    publish.allowed_permissions = ('change',)


class PageAdminForm(forms.ModelForm):
    text = forms.CharField(
        required=False,
        label='Контент странциы',
        widget=CKEditorUploadingWidget
    )

    class Meta:
        model = Page
        fields = '__all__'


@admin.register(Page)
class PageAdmin(ActionPublish):
    list_display = ('title', 'published', 'registration_required', 'id')
    list_filter = ('published', 'template')
    list_editable = ('published', 'registration_required')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    form = PageAdminForm
    save_on_top = True
    actions = ['unpublish', 'publish']
    # readonly_fields = ('published_date',)
