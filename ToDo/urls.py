from django.urls import path

from .views import * 


urlpatterns = [
    path('<int:pk>',DetailsTodo.as_view()),
    path('',todoList.as_view()),
    path('create',CreateTodo.as_view()),
    path('delete/<int:pk>',DeleteTodo.as_view()),
    
]
