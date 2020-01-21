from django import template

from menu.models import MenuItem

register = template.Library()


def get_menu_item(menu):
    return MenuItem.objects.filter(
        menu__name=menu,
        menu__published=True,
        published=True
    )


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def menu_item(context, menu, template='menu/menu_item_tag.html'):
    return {
        'template': template,
        'items': get_menu_item(menu)
    }


@register.simple_tag(takes_context=True)
def for_menu_item(context, menu):
    return get_menu_item(menu)
