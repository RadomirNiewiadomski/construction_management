import json

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Construction, Report, OperationalActivity


class IndexView(TemplateView):
    template_name = "index.html"


class ConstructionListView(ListView):
    model = Construction
    template_name = "manage_constructions.html"
    context_object_name = "constructions"


class ConstructionDetailView(DetailView):
    model = Construction
    template_name = "detail_construction.html"
    centext_object_name = "construction"


class ReportListView(ListView):
    model = Report
    template_name = "manage_reports.html"
    context_object_name = "reports"


class ReportDetailView(DetailView):
    model = Report
    template_name = "detail_report.html"
    centext_object_name = "report"


class OperationalActivitiesListView(ListView):
    model = OperationalActivity
    template_name = "manage_operational_activities.html"
    context_object_name = "operational_activities"


class OperationalActivityDetailView(DetailView):
    model = Construction
    template_name = "detail_operational_activity.html"
    centext_object_name = "operational_activity"
