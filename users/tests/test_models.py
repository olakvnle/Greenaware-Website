from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

class UserAccountManagerTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(email='normal@user.com', password='foo', first_name='Normal', last_name='User')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password('foo'))
        self.assertEqual(user.get_full_name(), 'Normal User')

    def test_create_user_no_email(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password='foo')

    def test_create_user_with_normalized_email(self):
        user = User.objects.create_user(email='TEST@EMAIL.COM', password='foo')
        self.assertEqual(user.email, 'test@email.com')

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser('super@user.com', 'foo')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class UserAccountModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='user@test.com', first_name='Test', last_name='User', password='testpass123')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'user@test.com')

    def test_get_full_name(self):
        self.assertEqual(self.user.get_full_name(), 'Test User')
