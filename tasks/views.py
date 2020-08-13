from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView,
    DeleteView,
    )

from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'all_task.html'
    ordering = ['-date']

class CreateTaskView(CreateView):
    model = Task
    template_name = 'add_task.html'
    fields = ('title', 'body',)

class DetailTaskView(DetailView):
    model = Task
    template_name = 'detail_task.html'

class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'edit_task.html'
    fields = ('title', 'body',)

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('all_task')