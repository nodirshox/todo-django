from django.urls import path

from .views import (
    TaskListView, 
    CreateTaskView, 
    DetailTaskView, 
    UpdateTaskView,
    DeleteTaskView,
    )

urlpatterns = [
    path('', TaskListView.as_view(), name='all_task'),
    path('add/', CreateTaskView.as_view(), name='add_task'),
    path('<int:pk>/', DetailTaskView.as_view(), name='detail_task'),
    path('<int:pk>/edit/', UpdateTaskView.as_view(), name='update_task'),
    path('<int:pk>/delete/', DeleteTaskView.as_view(), name='delete_task'),
]