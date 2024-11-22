from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from unittest.mock import patch


class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('user.viewsets.send_mail')
    def test_create_user_sends_invitation_email(self, mock_send_mail):
        """Test creating a user triggers sending an invitation email."""
        payload = {
            "email": "testuser@example.com",
            "password": "securepassword123",
            "first_name": "Test",
            "last_name": "User",
        }
        response = self.client.post('/user/api/create/', payload)

        # Sprawdzamy, czy użytkownik został stworzony
        self.assertEqual(response.status_code, 201)

        # Sprawdzamy, czy send_mail został wywołany raz
        self.assertTrue(mock_send_mail.called)
        self.assertEqual(mock_send_mail.call_count, 1)

        # Sprawdzamy parametry przekazane do send_mail
        mock_send_mail.assert_called_with(
            subject="Welcome to Construction Management",
            message=mock_send_mail.call_args[1]['message'],  # Wyciągnięcie wiadomości
            from_email="noreply@constructionmanagement.com",
            recipient_list=["testuser@example.com"],
            fail_silently=False,
        )
