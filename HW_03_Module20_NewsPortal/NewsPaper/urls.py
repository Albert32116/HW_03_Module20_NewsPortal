from django.contrib import admin
from django.urls import include, path

from news.views import ArticleCreate, ArticleUpdate, ArticleDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('sign.urls')),
    path('news/', include('news.urls')),

    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
