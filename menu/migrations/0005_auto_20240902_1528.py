# Generated by Django 3.2.19 on 2024-09-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20240902_1512'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='menuitem',
            constraint=models.UniqueConstraint(fields=('menu', 'name'), name='unique_menuitem_name_in_menu'),
        ),
        migrations.AddConstraint(
            model_name='menuitem',
            constraint=models.UniqueConstraint(fields=('menu', 'named_url'), name='unique_menuitem_slug_in_menu'),
        ),
    ]
