import django_filters
from .models import Product, NewsPortal
from django import forms


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class ProductFilter(django_filters.FilterSet):
    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Product
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'name': ['icontains'],
            # количество товаров должно быть больше или равно
            'quantity': ['gt'],
            'price': [
                'lt',  # цена должна быть меньше или равна указанной
                'gt',  # цена должна быть больше или равна указанной
            ],
        }


# ------------------------------------------------------------------------------------------------------
# Создаем свой набор фильтров для модели News.

class NewsFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(field_name='sort_date_of_publication',
                                     widget=forms.DateInput(attrs={'type': 'date'}), label='Дата',
                                     lookup_expr='date__gte')

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = NewsPortal
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'article_title': ['icontains', 'startswith'],

            # количество товаров должно быть больше или равно
            'article_author': ['startswith',
                               'endswith']
        }
