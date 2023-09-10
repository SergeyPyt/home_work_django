from django.shortcuts import render
from .models import TodoListItem
from django.views.generic.list import ListView


class TodoListView(ListView):
    model = TodoListItem
    template_name = "index.html"
