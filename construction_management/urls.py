from django.urls import path

from .views import ConstructionView

app_name = 'reviews'

urlpatterns = [
    path('', ConstructionView.as_view(), name='index'),
]
