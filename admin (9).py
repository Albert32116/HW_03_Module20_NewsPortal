{% extends 'flatpages/default.html' %}
{% load socialaccount %}

{% block content %}
<h2>Вход в систему</h2>
<hr>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Войти">
</form>

<p>
    <a href="{% url 'account_signup' %}">Регистрация</a>
</p>

<p>
    <a href="{% provider_login_url 'yandex' %}">Войти через Yandex</a>
</p>
{% endblock content %}
