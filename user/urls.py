from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from . import viewsets

app_name = 'user'

urlpatterns = [
    # Dashboard
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    # User management for admin
    path('admin/users/', views.user_list, name='user_list'),
    path('admin/users/create/', views.create_user, name='create_user'),
    path('admin/users/<int:user_id>/edit/', views.edit_user, name='edit_user'),
    path('admin/users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    path('update/<int:pk>/', viewsets.UpdateUserView.as_view(), name='update-user'),
    # Login, logout, and registration
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('activate/', viewsets.ActivateUserView.as_view(), name='activate'),
    # API endpoints
    path('api/create/', viewsets.CreateUserView.as_view(), name='api-create'),
    path('api/token/', viewsets.CreateTokenView.as_view(), name='api-token'),
    path('api/me/', viewsets.ManageUserView.as_view(), name='api-me'),
]
