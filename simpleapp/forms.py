from django import forms
from .models import NewsPortal
from django.core.exceptions import ValidationError

from allauth.account.forms import SignupForm  # форму регистрации SignupForm из коробки allauth
from django.contrib.auth.models import Group  # импорт созданных групп

# ------------------------------------------------------------------------------------------------------------------

class NewForm(forms.ModelForm):
    class Meta:
        model = NewsPortal
        # fields = '__all__' для всех форм в модели models.py, либо можно ввести тет поля которые мы будим менять
        # добавлять или удалять, эта функция будит доступная и для пользователя
        fields = ['article_title', 'article_author', 'article_description', 'news_category']

    def clean(self):
        cleaned_data = super().clean()
        article_title = cleaned_data.get("article_title")
        article_description = cleaned_data.get("article_description")

        if article_title == article_description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

# Скрипт, который при успешном прохождении регистрации добавлять присоединение к базовой группе пользователей
class CommonSignupForm(SignupForm):

    def save(self, request):
        user = super(CommonSignupForm, self).save(request)  # вызываем этот же метод класса-родителя сохранение в
        # модель User
        common_group = Group.objects.get(name='common')  # получаем объект модели группы common
        common_group.user_set.add(user)  # через атрибут user_set, возвращающий список всех пользователей этой группы,
        # мы добавляем нового пользователя в эту группу
        return user  # возвращение объекта модели User по итогу выполнения функции

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо формы по умолчанию, необходимо добавить
# строчку в файл настроек проекта settings.py