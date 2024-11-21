"""
Django command to create default admin.
"""

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to create default admin (in DEV mode)."""

    def handle(self, *arg, **options):
        admin_user = get_user_model().objects.filter(email="admin@example.com", role='ADMINISTRATOR')
        if admin_user.exists():
            self.stdout.write(self.style.SUCCESS('This admin user already exists.'))
        else:
            get_user_model().objects.create_superuser(
                email="admin@example.com",
                password="password123",
                first_name='Administrator',
                last_name='Admin',
            )
            self.stdout.write(self.style.SUCCESS('Admin user was created.'))
