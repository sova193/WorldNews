# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  # импортируем для удаления новостей
from .models import Product, NewsPortal
from datetime import datetime
from .filters import ProductFilter, NewsFilter
from .forms import ProductForm, NewForm  # для создания продуктов через функцию forms.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group


class ProductsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Product
    # Поле, которое будет использоваться для сортировки объектов
    ordering = 'name'  # сортировка по расположению в порядке возрастания, или убывания '-name'

    # queryset = Product.objects.filter(
    #     price__lt=65990
    # ).order_by('name')  # отсортировать по цене ниже чем 50000 и с помощью .order_by добавить другую
    # # сортировку ordering = 'name'

    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/products.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2  # вот так мы можем указать количество записей на странице

    # Переопределяем функцию получения списка товаров
    def __init__(self):
        self.filterset = None

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юнете ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.

        self.filterset = ProductFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Снижения цен не будет!'

        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# ProductDetail, которое будет выдавать информацию об одном товаре
class ProductDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Product
    # Используем другой шаблон — product.html
    template_name = 'flatpages/product.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Снижение цен не будет!'
        return context


# Create your views here.

# Добавляем новое представление для создания товаров.
class ProductCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = ProductForm
    # модель товаров
    model = Product
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/product_edit.html'


# ______________________________________________________________________________________________________________

class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = NewsPortal
    # ___________________________________________________________
    ordering = '-sort_date_of_publication'
    # Здесь будит Фильтрация
    # по новизне новости
    # ___________________________________________________________
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'flatpages/news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'

    paginate_by = 10  # вот так мы можем указать количество записей на странице

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юнете ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.

        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.

        context['next_sale'] = 'Лучшие новости из достоверных источников!'

        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset

        return context


# NewsDetail, которое будет выдавать информацию об одной новости
class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = NewsPortal
    ordering = '-sort_date_of_publication'
    # Используем другой шаблон — new.html
    template_name = 'flatpages/new.html'
    # Название объекта, в котором будет выбранный пользователем новость
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = 'Дальше будет интереснее'
        return context


# Добавляем новое представление для создания новости.
class NewCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель товаров
    model = NewsPortal
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/post/new/create/':
            new.news_category_id = 1
        elif self.request.path == '/post/article/create/':
            new.news_category_id = 2
        new.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

# Авторизация пользователя для изменения данных и их обновление с помощью LoginRequiredMixin. Так же
# прописываем settings.py переменная LOGIN_URL с возвратом на страницу после успешной авторизации. Импортируем так
# же from django.contrib.auth.mixins import LoginRequiredMixin

# Добавляем обновление новости и статьи.
class NewUpdate(LoginRequiredMixin, UpdateView):
    # Указываем нашу разработанную форму
    form_class = NewForm
    # модель товаров
    model = NewsPortal
    # и новый шаблон, в котором используется форма.
    template_name = 'flatpages/new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        if self.request.path == '/post/new/create/':
            new.news_category_id = 1
        elif self.request.path == '/post/article/create/':
            new.news_category_id = 2
        new.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

# Представление удаляющее товар.
class NewDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('simpleapp.delete_newsportal')

    model = NewsPortal
    template_name = 'flatpages/new_delete.html'
    success_url = reverse_lazy('new_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

def upgrade_me(request):
    user = request.user
    author_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        author_group.user_set.add(user)
    return redirect('/profile/')

def profile(request):
    context = {'is_not_author': not request.user.groups.filter(name='authors').exists()}
    return render(request, 'flatpages/profile.html', context)