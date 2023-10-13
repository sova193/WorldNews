from django.contrib import admin
from .models import *    # импортируем категории(классы из models)


class NewsCategoryInline(admin.TabularInline):
    model = NewsPortalCategory
    extra = 1

def delete_all_chosen(modeladmin, request, queryset):
    queryset.delete()
    delete_all_chosen.short_description = 'Удалить все выбранные позиции'

class NewsPortalAdmin(admin.ModelAdmin):
    model = NewsPortal
    inlines = (NewsCategoryInline,)
    list_display = ('article_title', 'article_author', 'sort_date_of_publication')  # Отображение определенных
    # характеристик
    list_filter = ('article_title', 'article_author', 'sort_date_of_publication')  # Фильтры
    search_fields = ('article_title', 'category__article_title')  # Поиск
    actions = [delete_all_chosen]

admin.site.register(NewsCategory)
admin.site.register(NewsPortalCategory)
admin.site.register(NewsPortal, NewsPortalAdmin)


# Register your models here.
