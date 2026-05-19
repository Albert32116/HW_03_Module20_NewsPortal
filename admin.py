from django import template


register = template.Library()

BAD_WORDS = [
    'редиска',
    'Редиска',
]


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Фильтр censor можно применять только к строкам')

    result = value
    for word in BAD_WORDS:
        result = result.replace(word, word[0] + '*' * (len(word) - 1))

    return result
