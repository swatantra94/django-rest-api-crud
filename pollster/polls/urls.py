from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('',views.apioverview, name = "api-overview"),
    path('task-list/',views.taskList, name = "task-list"),
    path('task-detail/<str:pk>/',views.taskDetail, name = "task-detail"),
    path('task-create/',views.taskCreate, name = "task-create"),
    path('task-detail/<str:pk>/',views.taskDetail, name = "task-detail"),
]
