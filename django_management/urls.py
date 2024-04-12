from django.contrib import admin
from django.urls import path

from views.health import health_check
from views.projects import (ProjectListCreateAPIView,
                            ProjectRetrieveUpdateDestroyAPIView)
from views.users import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from views.tasks_view import TasksListCreateAPIView, TasksRetrieveUpdateDestroyAPIView
from views.teams_view import TeamsListCreateAPIView, TeamsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/',
         UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/',
         ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),
    path('api/tasks/', TasksListCreateAPIView.as_view(), name='tasks-list'),
    path('api/tasks/<int:pk>/',
         TasksRetrieveUpdateDestroyAPIView.as_view(), name='tasks-detail'),
    path('api/teams/', TeamsListCreateAPIView.as_view(), name='teams-list'),
    path('api/teams/<int:pk>/',
         TeamsRetrieveUpdateDestroyAPIView.as_view(), name='teams-detail'),
]
