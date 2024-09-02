from django.contrib import admin
from dynamic_raw_id.admin import DynamicRawIDMixin

from menu.admin.forms import MenuItemInlineForm
from menu.models import Menu, MenuItem


class MenuItemInlineForMenu(DynamicRawIDMixin, admin.StackedInline):
    model = MenuItem
    extra = 0
    fk_name = 'menu'
    fields = ('name', 'parent', 'named_url')
    prepopulated_fields = {'named_url': ('name',)}
    dynamic_raw_id_fields = ('parent')


class MenuItemInlineForItem(DynamicRawIDMixin, admin.StackedInline):
    model = MenuItem
    form = MenuItemInlineForm
    fk_name = 'parent'
    extra = 0
    fields = ('name', 'named_url', 'parent',)
    prepopulated_fields = {'named_url': ('name',)}
    dynamic_raw_id_fields = ('menu', 'parent')


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    inlines = [MenuItemInlineForMenu]

    prepopulated_fields = {'slug': ('name',)}


class MenuItemAdmin(DynamicRawIDMixin, admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'named_url')
    list_filter = ('menu',)

    dynamic_raw_id_fields = ('menu', 'parent')

    search_fields = ('name', 'named_url',)

    prepopulated_fields = {'named_url': ('name',)}

    inlines = [MenuItemInlineForItem]


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
