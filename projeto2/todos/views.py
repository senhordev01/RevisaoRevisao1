from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Todo

class TodoListView(ListView):
    model = Todo
class TodoCreateView(CreateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy('todo_list')