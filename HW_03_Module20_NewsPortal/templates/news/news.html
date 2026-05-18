{% extends 'flatpages/default.html' %}
{% load custom_filters %}
{% load custom_tags %}

{% block title %}Новости{% endblock title %}

{% block content %}
<h2>Все новости</h2>

{% if user.is_authenticated and is_not_author %}
    <p>
        <a href="/news/upgrade/">
            <button>Стать автором!</button>
        </a>
    </p>
{% endif %}

<hr>

{% if news %}
    {% for post in news %}
        <h3><a href="{% url 'news_detail' post.id %}">{{ post.title|censor }}</a></h3>
        <p>{{ post.created_at|date:'d.m.Y' }}</p>
        <p>{{ post.content|censor|truncatechars:20 }}</p>
        <hr>
    {% endfor %}
{% else %}
    <h3>Новостей нет</h3>
{% endif %}

{% if page_obj.has_previous %}
    <a href="?{% url_replace page=1 %}">1</a>
    {% if page_obj.previous_page_number != 1 %}
        ...
        <a href="?{% url_replace page=page_obj.previous_page_number %}">
            {{ page_obj.previous_page_number }}
        </a>
    {% endif %}
{% endif %}

{{ page_obj.number }}

{% if page_obj.has_next %}
    <a href="?{% url_replace page=page_obj.next_page_number %}">
        {{ page_obj.next_page_number }}
    </a>
    {% if page_obj.paginator.num_pages != page_obj.next_page_number %}
        ...
        <a href="?{% url_replace page=page_obj.paginator.num_pages %}">
            {{ page_obj.paginator.num_pages }}
        </a>
    {% endif %}
{% endif %}
{% endblock content %}
