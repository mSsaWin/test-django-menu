from django.shortcuts import render, get_object_or_404

from menu.models import MenuItem


def home(request):
    return render(request, 'base.html')


def menuitem_detail(request, menu_slug, item_slug):
    item = get_object_or_404(MenuItem, menu__slug=menu_slug, named_url=item_slug)
    context = {
        'item_name': item.name,
        'request': request
    }
    return render(request, 'menu/menu_item.html', context)
