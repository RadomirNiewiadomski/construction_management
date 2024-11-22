"""
URL mappings for the user API.
"""

from django.urls import path

from user import viewsets

app_name = 'user-api'

urlpatterns = [
    path('create/', viewsets.CreateUserView.as_view(), name='create'),
    path('token/', viewsets.CreateTokenView.as_view(), name='token'),
    path('me/', viewsets.ManageUserView.as_view(), name='me'),
]
