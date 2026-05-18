# HW_03_Module20_NewsPortal

Продолжение проекта News Portal для модуля 20 «Создание контента и авторизация».

## Что сделано

- Подключён `django-allauth`.
- Добавлена регистрация и вход через `/accounts/login/` и `/accounts/signup/`.
- Добавлена возможность входа через Yandex.
- Созданы группы `common` и `authors`.
- Новые пользователи автоматически добавляются в группу `common`.
- Есть кнопка «Стать автором!».
- При нажатии пользователь добавляется в группу `authors`.
- Для группы `authors` добавлены права `news.add_post` и `news.change_post`.
- Создание и редактирование новостей/статей защищено через `PermissionRequiredMixin`.
- Страница профиля защищена через `LoginRequiredMixin`.

## Запуск

```bash
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Важные страницы

- `/news/` — список новостей.
- `/news/search/` — поиск.
- `/news/create/` — создание новости.
- `/news/<id>/edit/` — редактирование новости.
- `/articles/create/` — создание статьи.
- `/articles/<id>/edit/` — редактирование статьи.
- `/accounts/login/` — вход.
- `/accounts/signup/` — регистрация.
- `/sign/profile/` — профиль пользователя.

## Yandex OAuth

В админке нужно добавить Social application:

- Provider: Yandex
- Name: Yandex
- Client id: из кабинета Yandex OAuth
- Secret key: из кабинета Yandex OAuth
- Sites: `127.0.0.1:8000`

Redirect URL для Yandex:

```text
http://127.0.0.1:8000/accounts/yandex/login/callback/
```

## Проверка групп

После регистрации пользователь автоматически попадает в `common`.

На странице `/news/` авторизованный пользователь видит кнопку «Стать автором!». После нажатия он попадает в `authors` и получает возможность создавать и редактировать публикации.
