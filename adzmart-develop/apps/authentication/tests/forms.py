from django.test import TestCase
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from io import BytesIO

from apps.authentication.form import SupplierSignUpForm
from apps.authentication.models import User, Supplier

class BaseTest(TestCase):
    def setUp(self):
        self.post_dict = {
            'email': 'email@gmail.com',
            'first_name': 'Tola',
            'last_name': 'Abiodun',
            'phone_no': 2323989823,
            'company_name': 'Adzmart',
            'company_location': 'Lagos',
            'rc_number': 1234,
            'password1': 'sadioj123723',
            'password2': 'sadioj123723',
        }

        loaded_file = BytesIO(b"dummy bcode data: \x00\x01")
        loaded_file.name = 'test_file.xls'
        self.file_dict = {'government_id': SimpleUploadedFile(loaded_file.name, loaded_file.read())}
        self.user1 = User(email='test@gmail.com', password='password', first_name='firstname', last_name='last_name')
        self.user2 = User(email='tester@gmail.com', password='password', first_name='firstname', last_name='last_name')
        self.user1.save()
        self.user2.save()

        return super().setUp()

class TestForms(BaseTest):
    def test_supplier_reg_form(self):
        form = SupplierSignUpForm(self.post_dict, self.file_dict)
        print(form.errors)
        self.assertTrue(form.is_valid())
        self.assertEquals(form.clean_email() , form.cleaned_data["email"].lower())

    def test_supplier_reg_no_data(self):
        form  = SupplierSignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 10)

    def test_empty_form(self):
        form = SupplierSignUpForm()
        self.assertIn('email', form.fields)
        self.assertIn('first_name', form.fields)
    
    def test_email_already_exits_on_supplier_reg(self):
        post_dict = {
            'email': 'tester@gmail.com',
            'first_name': 'Tola',
            'last_name': 'Abiodun',
            'phone_no': 2323989823,
            'company_name': 'Adzmart',
            'company_location': 'Lagos',
            'rc_number': 1234,
            'password1': 'sadioj123723',
            'password2': 'sadioj123723',
        }

        form = SupplierSignUpForm(post_dict, self.file_dict)
        self.assertTrue(form.has_error('email'))
        self.assertIn('Email already exists', form.errors['email'])

    def test_company_name_already_exits_on_supplier_reg(self):
        # create suppliers
        supplier = Supplier(owner=self.user1, company_name=self.post_dict['company_name'], 
                            company_location=self.post_dict['company_location'], 
                            rc_number=self.post_dict['rc_number'])
        supplier.save()

        post_dict = {
            'email': 'email@gmail.com',
            'first_name': 'Tola',
            'last_name': 'Abiodun',
            'phone_no': 2323989823,
            'company_name': 'Adzmart',
            'company_location': 'Lagos',
            'rc_number': 1234,
            'password1': 'sadioj123723',
            'password2': 'sadioj123723',
        }

        form = SupplierSignUpForm(post_dict, self.file_dict)

        self.assertTrue(form.has_error('company_name'))
        self.assertIn('Company already exists', form.errors['company_name'])

    def test_company_rc_already_exits_on_supplier_reg(self):
        # create suppliers
        supplier = Supplier(owner=self.user1, company_name=self.post_dict['company_name'], 
                            company_location=self.post_dict['company_location'], 
                            rc_number=self.post_dict['rc_number'])
        supplier.save()

        post_dict = {
            'email': 'email@gmail.com',
            'first_name': 'Tola',
            'last_name': 'Abiodun',
            'phone_no': 2323989823,
            'company_name': 'Adzmart',
            'company_location': 'Lagos',
            'rc_number': 1234,
            'password1': 'sadioj123723',
            'password2': 'sadioj123723',
        }

        form = SupplierSignUpForm(post_dict, self.file_dict)

        self.assertTrue(form.has_error('rc_number'))
        self.assertIn('Company RC already exists', form.errors['rc_number'])
    
    def test_new_supplier_user_reg_response(self):
        request = HttpRequest()
        form = SupplierSignUpForm(self.post_dict, self.file_dict)
        response = self.client.post(reverse('authentication:login'), request.POST)
        self.assertEqual(response.status_code, 200)
