from django.contrib import admin
from django.urls import path
from views.users import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from views.health import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check, name='health_check'),
    path('api/users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
]
