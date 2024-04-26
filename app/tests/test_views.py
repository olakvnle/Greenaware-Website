from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

User = get_user_model()

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(password='12345', email='test@test.com')
        self.urls_to_templates = {
            'index': ('index', 'new/index.html'),
            'about': ('about', 'new/about.html'),
            'api': ('api', 'new/api.html'),
            'pricing': ('pricing', 'new/pricing.html'),
            'pricing_plan': ('pricing_plan', 'new/pricing_plan.html'),
            'contact': ('contact', 'new/contact.html'),
            'dashboard': ('dashboard', 'observer/dashboard.html'),
            'observation': ('observation', 'observer/observation.html'),
            'courses': ('courses', 'observer/course.html'),
            'users': ('users', 'observer/user.html')
        }

    def test_views_GET(self):
        for url_name, data in self.urls_to_templates.items():
            with self.subTest(url_name=url_name):
                if url_name in ['dashboard']:  # Views that require login
                    self.client.force_login(self.user)
                response = self.client.get(reverse(url_name))
                self.assertEquals(response.status_code, 200)
                self.assertTemplateUsed(response, data[1])
                self.client.logout()  # Ensure we log out before the next test case

    def test_dashboard_unauthenticated_access(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEquals(response.status_code, 302)  # Should redirect to login

# class TestEmailValidationView(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('email_validate')
#         User.objects.create_user(username='existing', email='alreadyexists@test.com', password='12345')

#     def test_email_validation_POST_invalid_email(self):
#         response = self.client.post(self.url, {'email': 'invalidemail'}, content_type='application/json')
#         self.assertEquals(response.status_code, 400)
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'email_error': 'Invalid Email'})

#     def test_email_validation_POST_existing_email(self):
#         response = self.client.post(self.url, {'email': 'alreadyexists@test.com'}, content_type='application/json')
#         self.assertEquals(response.status_code, 400)
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'email_error': 'Email already exists'})

#     def test_email_validation_POST_valid_email(self):
#         response = self.client.post(self.url, {'email': 'valid@test.com'}, content_type='application/json')
#         self.assertEquals(response.status_code, 200)
#         self.assertJSONEqual(str(response.content, encoding='utf8'), {'email_valid': True})
