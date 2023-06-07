from django import forms
from .models import Product, NewsPortal
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__' для всех форм в модели models.py, либо можно ввести тет поля которые мы будим менять
        # добавлять или удалять, эта функция будит доступная и для пользователя
        fields = ['name', 'description', 'quantity', 'category', 'price']

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        description = cleaned_data.get("description")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

# ------------------------------------------------------------------------------------------------------------------

class NewForm(forms.ModelForm):
    class Meta:
        model = NewsPortal
        # fields = '__all__' для всех форм в модели models.py, либо можно ввести тет поля которые мы будим менять
        # добавлять или удалять, эта функция будит доступная и для пользователя
        fields = ['article_title', 'article_author', 'article_description']    # , #'news_category'

    def clean(self):
        cleaned_data = super().clean()
        article_title = cleaned_data.get("article_title")
        article_description = cleaned_data.get("article_description")

        if article_title == article_description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

