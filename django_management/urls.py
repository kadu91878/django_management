from django.contrib import admin
from django.urls import path

from views.health import health_check
from views.projects import (ProjectListCreateAPIView,
                            ProjectRetrieveUpdateDestroyAPIView)
from views.users import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/projects/', ProjectListCreateAPIView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectRetrieveUpdateDestroyAPIView.as_view(), name='project-detail'),    
]
