from django.test import TestCase
from django.contrib.auth import get_user_model


# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        User=get_user_model()
        user=User.objects.create_user(username="will",email="will@email.com",password="test123")
        self.assertEqual(user.username,"will")
        self.assertEqual(user.email,"will@email.com")
        self.assertTrue(user.is_active)
        #self.assertFalse(user.if_staff)
    
    def test_create_superuser(self):
        User=get_user_model()
        user=User.objects.create_superuser(username="wi",email="wi@email.com",password="test1")
        self.assertEqual(user.username,"wi")
        self.assertEqual(user.email,"wi@email.com")
        
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_superuser)

