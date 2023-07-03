from django.contrib import admin
from .models import *    # импортируем категории(классы из models)


class NewsCategoryInline(admin.TabularInline):
    model = NewsPortalCategory
    extra = 1

class NewsPortalAdmin(admin.ModelAdmin):
    model = NewsPortal
    inlines = (NewsCategoryInline,)

# Приложение с новостями
admin.site.register(NewsCategory)
admin.site.register(NewsPortalCategory)
admin.site.register(NewsPortal, NewsPortalAdmin)


# Register your models here.
