"""
URL mappings for the user login.
"""

from django.urls import path
from django.contrib.auth.views import LogoutView

from user import views

app_name = 'user-login'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
