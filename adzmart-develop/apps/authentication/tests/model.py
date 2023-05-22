from django.test import TestCase
from apps.authentication.models import User
from django.conf import settings
import os

class TestUserModel(TestCase):

    def test_creates_user(self):
        user=User.objects.create_user(email='tola.adet@gmail.com', password='123ERTY', first_name='Tola', last_name='Abiodun', phone_no='090876237821')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'tola.adet@gmail.com')
        self.assertEqual(str(user.email), 'tola.adet@gmail.com')
        
    def test_creates_super_user(self):
        user=User.objects.create_superuser(email='tola.adet@gmail.com', password='123ERTY', first_name='Tola', last_name='Abiodun', phone_no='090876237821')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'tola.adet@gmail.com')

    def test_custom_user_model_str(self):
        email = User.objects.create(email='email')
        first_name = User.objects.create(first_name='first_name')
        last_name = User.objects.create(last_name='last_name')
        password = User.objects.create(password='password')
        password = User.objects.create(password='password')
        
        self.assertEqual(str(email), 'email')

    
    def test_raises_value_error_when_no_email_is_supplied_for_a_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_user(email=None, password='123ERTY', first_name='Tola', last_name='Abiodun', phone_no='090876237821')
            self.assertEqual(str(exception_context), 'Email is required.')

    def test_raises_value_error_when_no_email_is_supplied_for_a_super_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_superuser(email=None, password='123ERTY', first_name='Tola', last_name='Abiodun', phone_no='090876237821')
            self.assertEqual(str(exception_context), 'Superusers must have a password.')

    def test_raises_value_error_when_no_password_is_supplied_for_a_super_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_superuser(email='tola.adet@gmail.com', password=None, first_name='Tola', last_name='Abiodun', phone_no='090876237821')
            self.assertEqual(str(exception_context), 'Superusers must have a password.')

    def test_raises_value_error_when_no_first_name_is_supplied_for_a_super_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_superuser(email='tola.adet@gmail.com', password='1234TY', first_name=None, last_name='Abiodun', phone_no='090876237821')
            self.assertEqual(str(exception_context), 'Superusers must have a first_name.')

    def test_raises_value_error_when_no_last_name_is_supplied_for_a_super_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_superuser(email='tola.adet@gmail.com', password='1234TY', first_name='Tola', last_name=None, phone_no='090876237821')
            self.assertEqual(str(exception_context), 'Superusers must have a last name.')

    def test_raises_value_error_when_no_phone_no_is_supplied_for_a_super_user(self):
        with self.assertRaises(ValueError) as exception_context:
            User.objects.create_superuser(email='tola.adet@gmail.com', password='1234TY', first_name='Tola', last_name='Abiodun', phone_no=None)
            self.assertEqual(str(exception_context), 'Superusers must have a phone number.')
