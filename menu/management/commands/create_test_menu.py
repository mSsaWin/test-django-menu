from django.core.management.base import BaseCommand
from menu.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Создает три меню с вложенными пунктами меню, включая третий уровень вложенности'

    def handle(self, *args, **kwargs):
        menus_data = [
            {
                'name': 'Главное меню',
                'items': [
                    {'name': 'Страничка', 'children': []},
                    {'name': 'О нас', 'children': [
                        {'name': 'Наша команда', 'children': []},
                        {'name': 'История', 'children': [
                            {'name': 'Основатели', 'children': []},
                            {'name': 'Вехи', 'children': []}
                        ]}
                    ]}
                ]
            },
            {
                'name': 'Меню услуг',
                'items': [
                    {'name': 'Услуги', 'children': [
                        {'name': 'Консалтинг', 'children': [
                            {'name': 'Бизнес консалтинг', 'children': []},
                            {'name': 'ИТ консалтинг', 'children': []}
                        ]},
                        {'name': 'Поддержка', 'children': [
                            {'name': 'Поддержка клиентов', 'children': []},
                            {'name': 'Техническая поддержка', 'children': []}
                        ]}
                    ]}
                ]
            },
            {
                'name': 'Контактное меню',
                'items': [
                    {'name': 'Связаться с нами', 'children': [
                        {'name': 'Наш адрес', 'children': []},
                        {'name': 'Телефон', 'children': []},
                        {'name': 'Социальные сети', 'children': [
                            {'name': 'Facebook', 'children': []},
                            {'name': 'Twitter', 'children': []},
                            {'name': 'LinkedIn', 'children': []}
                        ]}
                    ]}
                ]
            }
        ]

        for menu_data in menus_data:
            menu = Menu.objects.create(name=menu_data['name'])
            self.create_menu_items(menu, menu_data['items'])

        self.stdout.write(self.style.SUCCESS('Три меню с вложенными пунктами меню успешно созданы!'))

    def create_menu_items(self, menu, items, parent=None):
        for item_data in items:
            item = MenuItem.objects.create(
                menu=menu,
                name=item_data['name'],
                parent=parent
            )

            if item_data['children']:
                self.create_menu_items(menu, item_data['children'], parent=item)
