import json

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Construction, Report, OperationalActivity


class ConstructionListView(ListView):
    model = Construction
    template_name = "manage_construcion.html"
    context_object_name = "constructions"


class ReportListView(ListView):
    model = Report
    template_name = "manage_reports.html"
    context_object_name = "reports"


class OperationalActivitiesListView(ListView):
    model = OperationalActivity
    template_name = "manage_operational_activities.html"
    context_object_name = "operational_activities"
