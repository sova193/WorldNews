from django import template

register = template.Library()

# добавляем возможность выбирать
CURRENCIES_SYMBOLS = {
    'rub': 'Р',
    'usd': '$',
    'euro': 'Euro'
}


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def currency(value, code='rub'):
    """
   Value: значение, к которому нужно применить фильтр
   """
    postfix = CURRENCIES_SYMBOLS[code]
    # Возвращаемое функцией значение подставится в шаблон.
    return f'{value} {postfix}'
