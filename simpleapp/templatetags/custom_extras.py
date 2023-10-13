from django import template

register = template.Library()

# из собственных фильтров
@register.filter
def lower(value):
    return value.lower()

# из собственных фильтров
@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

# из собственных тегов
@register.simple_tag(takes_context=True)
def func(context, other_arg):
    pass

# из собственных тегов
@register.simple_tag(takes_context=True, name="tagname")
def func(context, other_arg):
    pass

# Задание 16.2.6
# Реализуйте фильтр, который заменяет все буквы кроме первой и последней на «*» у слов из списка «нежелательных».
# Предполагается, что в качестве аргумента гарантированно передается текст, и слова разделены пробелами. Можно считать,
# что запрещенные слова находятся в списке forbidden_words.

forbidden_words = ['Администратор']
@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in forbidden_words:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)
    return " ".join(result)