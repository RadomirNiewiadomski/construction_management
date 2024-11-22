from django.urls import path
from django.views.generic import TemplateView

from .views import ConstructionListView, ReportListView, OperationalActivitiesListView

app_name = 'construction_management'

urlpatterns = [
    path('', TemplateView.as_view(), name='index'),
    path('manage_constructions/', ConstructionListView.as_view(), name='manage_constructions'),
    path('manage_reports/', ReportListView.as_view(), name='manage_reports'),
    path(
        'manage_operational_activities/',
        OperationalActivitiesListView.as_view(),
        name='manage_operational_activities',
    ),
]
