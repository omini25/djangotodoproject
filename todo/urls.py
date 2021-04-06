from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_todo_items),
    path('insert/', views.list_todo_insert, name='list_todo_insert')
]
