"""
URL configuration for Task_Quest project.
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
  path('', views.home_page, name='home'),
  path('calendar/', views.calendar, name='calendar'),
  path('tasks/', views.TaskListView.as_view(), name='task-list'),
  path('addtask/', views.create_task, name='add-task'),
  path('game/', views.start_game, name='quest-game'),
  path('complete-task/<int:task_id>/', views.complete_task, name='complete_task'),
  path('remove-task/<int:task_id>/', views.remove_task, name='remove_task'),

]

#urlpatterns  +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)