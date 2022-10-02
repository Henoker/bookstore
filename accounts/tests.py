import email
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='will', email='will@yahoo.com', password='testpass123'
        )
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@yahoo.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin', email='admin@yahoo.com', password='testpass123'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@yahoo.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
