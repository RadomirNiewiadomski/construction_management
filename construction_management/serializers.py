"""
Serializers for menu API.
"""

from rest_framework import serializers

from construction_management.models import Construction, Report, OperationalActivity


class OperationalActivitySerializer(serializers.ModelSerializer):
    """Serializer for Operational Activity."""

    class Meta:
        model = OperationalActivity
        fields = '__all__'


class ConstructionSerializer(serializers.ModelSerializer):
    """Serializer for Construction."""

    class Meta:
        model = Construction
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    """Serializer for Report."""

    class Meta:
        model = Report
        fields = '__all__'


class ConstructionDetailSerializer(ConstructionSerializer):
    """Serializer for Construction detail view."""

    class Meta:
        model = Construction
        fields = [
            'id',
            'name',
            'localization',
            'working_hours',
        ]
        read_only_fields = ['id']


class ReportDetailSerializer(ReportSerializer):
    """Serializer for Report detail view."""

    class Meta:
        model = Report
        fields = [
            'id',
            'created_at',
            'construction',
            'author',
            'operational_activity',
            'content',
            'images',
            'modified_date',
        ]
        read_only_fields = ['id']


class ReportImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to Report."""

    class Meta:
        model = Report
        fields = ['id', 'images']
        read_only_fields = ['id']
        extra_kwargs = {'images': {'required': 'True'}}
