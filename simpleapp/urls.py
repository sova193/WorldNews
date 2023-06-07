from django.urls import path
# Импортируем созданное нами представление
from .views import ProductsList, ProductDetail, NewsList, NewsDetail, ProductCreate, NewCreate, NewUpdate, NewDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   # Отображение всех продуктов
   path('', ProductsList.as_view()),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения

   #path('<int:pk>', ProductDetail.as_view()),

   # просмотр продуктов по id
   path('<int:pk>', ProductDetail.as_view(), name='product_detail'),

   # для создания товара в Products
   path('create/', ProductCreate.as_view(), name='product_create'),

   # Отображение всех новостей и статей
   path('post/', NewsList.as_view()),
   #path('post/<int:pk>', NewsDetail.as_view()),

   # просмотр статей и новостей подробно по id
   path('post/<int:pk>', NewsDetail.as_view(), name='new_detail'),

   # для создания новости через форму Новость
   path('post/new/create/', NewCreate.as_view(), name='new_create'),

   # для создания Статьи через форму Новость
   path('post/article/create/', NewCreate.as_view(), name='new_create'),

   # форма для обновления Новости
   path('post/new/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для обновления Статьи
   path('post/article/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для удаления Новости
   path('post/new/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),

   # форма для удаления Статьи
   path('post/article/<int:pk>/delete/', NewDelete.as_view(), name='new_delete')
]