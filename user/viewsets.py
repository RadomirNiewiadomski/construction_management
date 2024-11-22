"""
Views for the user API.
"""

from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.urls import reverse

from user.serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        """Create a user and send an invitation email."""
        user = serializer.save()
        activation_url = (
            f"{self.request.build_absolute_uri(reverse('user:activate'))}?token={user.auth_token.key}"
        )
        send_mail(
            subject="Welcome to Construction Management",
            message=f"Hello {user.first_name},\n\nPlease activate your account by clicking the link below:\n{activation_url}",
            from_email="noreply@constructionmanagement.com",
            recipient_list=[user.email],
            fail_silently=False,
        )


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class ActivateUserView(APIView):
    """Activate user account via token."""

    def get(self, request):
        token = request.query_params.get('token')
        try:
            user = Token.objects.get(key=token).user
            user.is_active = True
            user.save()
            return Response({'message': 'Account activated successfully!'})
        except Token.DoesNotExist:
            return Response({'error': 'Invalid or expired token.'}, status=400)


class UpdateUserView(generics.UpdateAPIView):
    """Update user details by admin."""

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def patch(self, request, *args, **kwargs):
        """Partially update user details."""
        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Fully update user details."""
        return super().put(request, *args, **kwargs)
