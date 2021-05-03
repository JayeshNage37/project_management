
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('homepage', views.home),
    path('project', views.projecttable.as_view()),
    path('project/p/<int:project_id>/', views.projectupdatetable.as_view()),
    path('project/<int:project_id>/', views.tasktable.as_view()),
    path('project/<int:project_id>/task', views.tasktable.as_view()),
    path('project/<int:project_id>/task/<int:task_id>/', views.tasktupdateable.as_view()),
   
]