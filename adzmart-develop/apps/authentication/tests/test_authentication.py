from django.test import TestCase
from django.urls import reverse 

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("authentication:register")

        return super().setUp()

class SupplierBaseTest(TestCase):
    def setUp(self):
        self.supplier_register_url = reverse("authentication:supplier_register")

        return super().setUp()

class RegisterSupplierTest(SupplierBaseTest):
    def test_register_buyer_page_loads(self):
        response = self.client.get(self.supplier_register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/supplier_register.html")
