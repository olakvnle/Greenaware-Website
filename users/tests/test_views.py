from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.messages import get_messages
from django.contrib.auth.tokens import PasswordResetTokenGenerator


import json

User = get_user_model()
account_activation_token = PasswordResetTokenGenerator()

def create_user(email='user@example.com', password='testpassword123', is_active=False, is_observer=True):
    user = User.objects.create_user(email=email, first_name='John', last_name='Doe', password=password)
    user.is_active = is_active
    user.is_observer = is_observer
    user.save()
    return user
#
# class ObserverRegistrationViewTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('observer')
#         self.valid_payload = {
#             'email': 'newuser@example.com',
#             'first_name': 'Test',
#             'last_name': 'User',
#             'password': 'validpassword123',
#             're_password': 'validpassword123'
#         }
#
#     def test_get_observer_registration_page(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'new/observer.html')
#
#     def test_post_observer_registration_valid(self):
#         response = self.client.post(self.url, json.dumps(self.valid_payload), content_type='application/json')
#         self.assertEqual(response.status_code, 200)
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'success': 'Account created successfully'})
#
#     def test_post_observer_registration_email_exists(self):
#         create_user(email='newuser@example.com')  # Create a user with the same email as in valid_payload
#         response = self.client.post(self.url, json.dumps(self.valid_payload), content_type='application/json')
#         self.assertEqual(response.status_code, 400)
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'email_error': 'Email already registered'})

class LoginViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('login')
        self.user = create_user(is_active=True)  # Create an active user for login tests

    def test_get_login_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new/login.html')


    def test_post_login_valid_credentials(self):
        response = self.client.post(self.url, json.dumps({'email': 'user@example.com', 'password': 'testpassword123'}), content_type='application/json')
        self.assertIn('msg', response.json())  # Checks if 'msg' key is in the JSON response
        self.assertEqual(response.json()['msg'], '/observer/dashboard')


    # def test_post_login_invalid_credentials(self):
    #     response = self.client.post(self.url, json.dumps({'email': 'user@example.com', 'password': 'wrongpassword'}), content_type='application/json')
    #     self.assertEqual(response.status_code, 400)
    #     self.assertJSONEqual(str(response.content, encoding='utf8'), {'error': 'This credential is not valid'})

# class ActivateObserverViewTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.user = create_user()
#         uidb64 = urlsafe_b64encode(force_bytes(self.user.pk))
#         token = account_activation_token.make_token(self.user)
#         self.url = reverse('activation', kwargs={'uidb64': uidb64, 'token': token})

    # def test_get_activate_user_valid(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, 302)  # Assuming redirect to login page after activation
    #     self.user.refresh_from_db()
    #     self.assertTrue(self.user.is_active)

    # def test_get_activate_user_invalid_token(self):
    #     url = reverse('activation', kwargs={'uidb64': urlsafe_b64encode(force_bytes(self.user.pk)), 'token': 'bad-token'})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 302)  # Redirect, assuming invalid token message shown

