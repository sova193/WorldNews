from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, NewsDetail, NewCreate, NewUpdate, NewDelete, \
   upgrade_me, profile, AppointmentView, subscribe, unsubscribe, CategoryListView

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.

   # Отображение всех продуктов
   #path('', ProductsList.as_view()),   # если нам нужно создавать статью и новость отдельно, универсальный
   # путь http://127.0.0.1:8000/'' из project\urls.py
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения


   # Отображение всех новостей и статей, где 'new_list' это класс во views
   path('', NewsList.as_view(), name='new_list'),
   #path('post/<int:pk>', NewsDetail.as_view()),

   # просмотр статей и новостей подробно по id(где 'post/<int:pk>' это 'post/1 или 2 или 3 ...')
   path('<int:pk>', NewsDetail.as_view(), name='new_detail'),

   # для создания новости через форму Новость
   path('new/create/', NewCreate.as_view(), name='new_create'),

   # для создания Статьи через форму Новость
   path('article/create/', NewCreate.as_view(), name='new_create'),

   # форма для обновления(добавление) Новости
   path('new/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для обновления(добавление) Статьи
   path('article/<int:pk>/update/', NewUpdate.as_view(), name='new_update'),

   # форма для удаления Новости
   path('new/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),

   # форма для удаления Статьи
   path('article/<int:pk>/delete/', NewDelete.as_view(), name='new_delete'),

   # форма для шаблона стать автором
   path('upgrade/', upgrade_me, name='upgrade'),

   # путь формы для профиля
   path('profile/', profile, name='profile'),

   # Для записи человека куда либо
   path('appointment/', AppointmentView.as_view(), name='appointments'),

   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),

   path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),

   path('categories/<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
]