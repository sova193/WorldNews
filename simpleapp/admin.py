from django.contrib import admin
from .models import Category, Product, NewsCategory, NewsPortal    # импортируем категории(классы из models)

# Приложение с товарами
admin.site.register(Category)
admin.site.register(Product)

# Приложение с новостями
admin.site.register(NewsCategory)
admin.site.register(NewsPortal)
# Register your models here.
