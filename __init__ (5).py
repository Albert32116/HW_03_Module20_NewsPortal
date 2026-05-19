{% extends 'flatpages/default.html' %}

{% block title %}Редактирование{% endblock title %}

{% block content %}
<h2>Добавление / редактирование публикации</h2>
<hr>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Сохранить">
</form>
{% endblock content %}
