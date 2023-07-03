import django_filters
from .models import NewsPortal
from django import forms


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
