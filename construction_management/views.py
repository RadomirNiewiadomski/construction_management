import json

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Construction


class ConstructionView(ListView):
    model = Construction
    template_name = "index.html"
