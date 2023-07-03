# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
from django import template

register = template.Library()


def censor(value):
    bad_words = ['обезьян', 'Мартышки']
    for word in bad_words:
        value = value.replace(word, '*' * len(word))
    return value


register.filter('censor', censor)

