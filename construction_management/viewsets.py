"""
Viewsets for the construction management API.
"""

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from construction_management import serializers
from construction_management.models import Construction, Report, OperationalActivity


class OperationalActivityViewSet(viewsets.ModelViewSet):
    """View for manage operational activity APIs."""

    serializer_class = serializers.OperationalActivitySerializer
    queryset = OperationalActivity.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class ConstructionViewSet(viewsets.ModelViewSet):
    """View for manage construction APIs."""

    serializer_class = serializers.ConstructionDetailSerializer
    queryset = Construction.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return serializer class for request."""
        if self.action == 'list':
            return serializers.ConstructionSerializer

        return self.serializer_class


class ReportViewSet(viewsets.ModelViewSet):
    """View for manage report APIs"""

    serializer_class = serializers.ReportSerializer
    queryset = Report.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """Return serializer class for request."""
        if self.action == 'list':
            return serializers.ReportSerializer
        elif self.action == 'upload_image':
            return serializers.ReportImageSerializer

        return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to a book."""
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
