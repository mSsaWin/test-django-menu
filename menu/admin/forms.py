from django import forms


class MenuItemInlineForm(forms.ModelForm):
    # class Meta:
    #     model = MenuItem
    #     fields = ['name', 'named_url', 'parent', 'menu']

    def save(self, commit=True):
        # Получаем текущий экземпляр объекта
        instance = super(MenuItemInlineForm, self).save(commit=False)

        # Если у родителя (instance.parent) есть меню, то устанавливаем это меню
        if instance.parent:
            instance.menu = instance.parent.menu

        # Сохраняем объект, если commit=True
        if commit:
            instance.save()

        return instance
