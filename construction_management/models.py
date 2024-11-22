import os
import uuid

from django.db import models

from user.models import User

# Create your models here.


def report_image_file_path(instance, filename):
    """Generate file path for new book image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'report', filename)


class OperationalActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Operational Activity'
        verbose_name_plural = 'Operational Activities'

    def __str__(self):
        return self.name


class Construction(models.Model):
    name = models.CharField(max_length=255)
    localization = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    working_hours = models.CharField(max_length=50, default='08:00-17:00')
    is_archived = models.BooleanField(default=False)

    def archive(self):
        """Mark construction as archived."""
        self.is_archived = True
        self.save()

    def update_working_hours(self, hours):
        """Update working hours for the construction."""
        self.working_hours = hours
        self.save()

    def __str__(self):
        return self.name


class Report(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    operational_activity = models.ForeignKey(
        OperationalActivity, on_delete=models.CASCADE, blank=True, null=True
    )
    content = models.TextField()
    # TODO: change to upload multiple imgs (max 5)
    images = models.ImageField(null=True, blank=True, upload_to=report_image_file_path)
    # TODO: change modified_date to modify_history
    modified_date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f'By {self.author} at {self.created_at}'
