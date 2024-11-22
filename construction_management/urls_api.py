from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .viewsets import ConstructionViewSet, ReportViewSet, OperationalActivityViewSet

router = DefaultRouter()
router.register('construction', ConstructionViewSet)
router.register('report', ReportViewSet)
router.register('operational_activity', OperationalActivityViewSet)

app_name = 'construction_management-api'

urlpatterns = [
    path('', include(router.urls)),
]
