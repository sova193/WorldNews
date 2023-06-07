from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)   # названия товаров не должны повторяться

    description = models.TextField()

    quantity = models.IntegerField(validators=[MinValueValidator(0)])   # поле категории будет ссылаться на
    # модель категории

    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')  # все продукты в
    # категории будут доступны через поле products

    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):   # отображение описания товара на страничке в интернете, плюс стоимость товара
        return f'{self.name.title()}: {self.description[:100]} ({self.price})'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()

#______________________________________________________________________________________________________________

class NewsPortal(models.Model):
    sort_date_of_publication = models.DateTimeField(auto_now_add=True)
    article_title = models.CharField(max_length=50, unique=True)   # названия статьи не должны повторяться
    article_author = models.CharField(max_length=50)
    article_description = models.TextField()   # Текст статьи

    news_category = models.ForeignKey(to='NewsCategory', on_delete=models.CASCADE, related_name='news')   # все
    # новости в категории будут доступны через поле news

    def __str__(self):   # отображение описания товара на страничке в интернете
        return f'{self.article_title.title()}: {self.article_description[:500]}: {self.article_author.title()}'

    def get_absolute_url(self):
        return reverse('new_detail', args=[str(self.id)])    # для создания новости и статьи отдельно
        #return reverse('post/new_detail', args=[str(self.id)])


class NewsCategory(models.Model):
    # названия категорий тоже не должны повторяться
    article_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.article_title.title()

    # Create your models here.
