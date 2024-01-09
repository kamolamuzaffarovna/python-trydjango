from django.urls import path
from .views import (
    article_detail,
    article_list,
    article_create,
    article_create_form,
    article_change,
    article_delete,
)

app_name = 'article'

urlpatterns = [
    path('', article_list, name='list'),
    path('article/<slug:slug>', article_detail, name='detail'),
    path('article/create/', article_create, name='created'),
    path('article/create/form/', article_create_form, name='created-form'),
    path('article/change/form/<int:pk>/', article_change, name='change-form'),
    path('article/delete/form/<int:pk>/', article_delete, name='delete')
]