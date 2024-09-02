from django import template
from menu.models import MenuItem
from menu.utils import build_menu_tree

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_slug):
    try:
        menu_items = MenuItem.objects.select_related('menu', 'parent').filter(menu__slug=menu_slug).order_by(
            'parent_id', 'id')
        current_path = context['request'].path

        menu_tree = build_menu_tree(menu_items, current_path)

        return {
            'menu_tree': menu_tree,
            'request': context['request']
        }
    except MenuItem.DoesNotExist:
        return {
            'menu_tree': [],
            'request': context['request']
        }
