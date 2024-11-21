from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .viewsets import ConstructionViewSet, ReportViewSet

router = DefaultRouter()
router.register('construction', ConstructionViewSet)
router.register('report', ReportViewSet)

app_name = 'construction_management-api'

urlpatterns = [
    path('', include(router.urls)),
]
