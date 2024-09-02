from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse, NoReverseMatch
from menu.utils import slugify


class Menu(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        unique=True,
        blank=False,
        null=False
    )

    slug = models.SlugField(
        verbose_name=_("Slug"),
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        help_text=_("Field will be filled automatically if no value is specified.")
    )

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menu")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        verbose_name=_("Menu"),
        related_name='items',
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent"),
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=100,
        blank=False,
        null=False
    )

    named_url = models.SlugField(
        verbose_name=_("Named URL"),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("Field will be filled automatically if no value is specified.")
    )

    class Meta:
        verbose_name = _("Menu Item")
        verbose_name_plural = _("Menu Items")

        constraints = [
            UniqueConstraint(fields=['menu', 'name'], name='unique_menuitem_name_in_menu'),
            UniqueConstraint(fields=['menu', 'named_url'], name='unique_menuitem_slug_in_menu'),
        ]

    def save(self, *args, **kwargs):
        if not self.named_url:
            self.named_url = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            return reverse('menuitem_detail', kwargs={'menu_slug': self.menu.slug, 'item_slug': self.named_url})
        except NoReverseMatch:
            return "#"
