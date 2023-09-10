from django.contrib import admin
from django.urls import path
from todo.views import TodoListView
from todo.services import add_item, delete_item


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', TodoListView.as_view()),
    path('todo/add/', add_item),
    path('todo/delete/<int:item>', delete_item)
]
