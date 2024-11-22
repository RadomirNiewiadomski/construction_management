"""
Django admin customization.
"""

from django.contrib import admin

from construction_management.models import Construction, Report, OperationalActivity


admin.site.register(Construction)
admin.site.register(Report)
admin.site.register(OperationalActivity)
