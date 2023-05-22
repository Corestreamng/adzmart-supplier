from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from apps.catalog.models import Unit, UnitType, RadioUnit, TVUnit, CinemaUnit, PrintUnit
from apps.authentication.models import User, Supplier
from apps.catalog.views import (
    load_billboard_catalog,
    load_radio_catalog,
    load_tv_catalog,
    load_cinema_catalog,
    load_print_catalog,
)
import os


class LoadCatalogPageTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        #  create a Unit for a user
        self.unit_type = UnitType(name="Radio")
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.is_active = True
        self.supplier = Supplier(
            owner=self.user,
            company_name="Adzmart",
            company_location="Lagos",
            rc_number="23412",
        )
        self.supplier.is_verified = True

        self.user.save()
        self.supplier.save()
        self.user.supplier = self.supplier
        self.unit_type.save()
        self.user.save()

        self.unit = Unit.objects.create(
            name="OOH",
            unit_type=self.unit_type,
            adzmart_hash="1234FG",
            unit_info={"key": "value"},
            user_id=self.user.id,
        )
        self.unit.save()

        self.cinema_unit = CinemaUnit.objects.create(
            cinema="Silverbird",
            location="Ikeja Mall",
            rate_per_spot="15000",
            state="Lagos",
            user_id=self.user.id,
        )
        self.cinema_unit.save()

        self.print_unit = PrintUnit(
            user=self.user,
            coverage="National",
            publisher="Vanguard",
            title="Test",
            type="Color",
            size="Full Page",
            position="Special Position",
            rate=12530,
            agency_discount=234.98,
            amount=345.2,
            vat=235.6,
            total=3456.32,
        )

        self.print_unit.save()

    def test_billboard_catalog_url_exists_at_correct_location(self):
        record = User.objects.get(email="test@gmail.com")
        request = self.factory.get("catalog/billboard/")
        request.user = self.user
        self.client.login(email="test@gmail.com", password="password")
        response = load_billboard_catalog(request)
        self.assertEqual(response.status_code, 200)

    def test_billboard_catalog_template_name_correct(self):
        record = Unit.objects.get(user=self.user.id)
        request = self.factory.get("catalog/billboard/")
        request.user = record.user

        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_billboard_catalog"))
        self.assertTemplateUsed(response, "catalog/billboard/billboard_inventory.html")

    def test_billboard_catalog_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_billboard_catalog"))
        self.assertContains(response, '<h4 class="mt-4">Billboard Units</h4>')
        self.assertNotContains(response, "Not on the page")

    def test_radio_catalog_url_exists_at_correct_location(self):
        record = User.objects.get(email="test@gmail.com")
        request = self.factory.get("catalog/radio/")
        request.user = self.user
        self.client.login(email="test@gmail.com", password="password")
        response = load_radio_catalog(request)
        self.assertEqual(response.status_code, 200)

    def test_radio_catalog_template_name_correct(self):
        record = Unit.objects.get(user=self.user.id)
        request = self.factory.get("catalog/radio/")
        request.user = record.user

        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_radio_catalog"))
        self.assertTemplateUsed(response, "catalog/radio/inventory.html")

    def test_radio_catalog_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_radio_catalog"))
        self.assertContains(response, '<h4 class="mt-4">Spots</h4>')
        self.assertNotContains(response, "Not on the page")

    def test_radio_catalog_url_exists_at_correct_location(self):
        record = User.objects.get(email="test@gmail.com")
        request = self.factory.get("catalog/tv/")
        request.user = self.user
        self.client.login(email="test@gmail.com", password="password")
        response = load_tv_catalog(request)
        self.assertEqual(response.status_code, 200)

    def test_tv_catalog_template_name_correct(self):
        record = Unit.objects.get(user=self.user.id)
        request = self.factory.get("catalog/tv/")
        request.user = record.user

        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_tv_catalog"))
        self.assertTemplateUsed(response, "catalog/tv/inventory.html")

    def test_tv_catalog_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_tv_catalog"))
        self.assertContains(response, '<h4 class="mt-4">Spots</h4>')
        self.assertNotContains(response, "Not on the page")

    def test_cinema_catalog_url_exists_at_correct_location(self):
        record = User.objects.get(email="test@gmail.com")
        request = self.factory.get("catalog/cinema/")
        request.user = self.user
        self.client.login(email="test@gmail.com", password="password")
        response = load_cinema_catalog(request)
        self.assertEqual(response.status_code, 200)

    def test_cinema_catalog_template_name_correct(self):
        record = CinemaUnit.objects.get(user=self.user.id)
        request = self.factory.get("catalog/cinema/")
        request.user = record.user

        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_cinema_catalog"))
        self.assertTemplateUsed(response, "catalog/cinema/cinema_inventory.html")

    def test_cinema_catalog_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_cinema_catalog"))
        self.assertContains(response, '<h4 class="mt-4">Cinema Units</h4>')
        self.assertNotContains(response, "Not on the page")

    def test_print_catalog_url_exists_at_correct_location(self):
        record = User.objects.get(email="test@gmail.com")
        request = self.factory.get("catalog/print/")
        request.user = self.supplier.owner
        self.client.login(email="test@gmail.com", password="password")
        response = load_print_catalog(request)
        self.assertEqual(response.status_code, 200)

    def test_print_catalog_template_name_correct(self):
        record = PrintUnit.objects.get(user=self.user.supplier.owner)
        request = self.factory.get("catalog/print/")
        request.user = record

        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_print_catalog"))
        self.assertTemplateUsed(response, "catalog/print/print_inventory.html")

    def test_print_catalog_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:load_print_catalog"))
        self.assertContains(response, '<h4 class="mt-4">Print Units</h4>')
        self.assertNotContains(response, "Not on the page")


class UploadCatalogPageTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        #  create a Unit for a user
        self.unit_type = UnitType(name="Radio")
        self.user = User.objects.create_user(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.is_active = True
        self.supplier = Supplier(
            owner=self.user,
            company_name="Adzmart",
            company_location="Lagos",
            rc_number="23412",
        )
        self.supplier.is_verified = True

        self.user.save()
        self.supplier.save()
        self.user.supplier = self.supplier
        self.unit_type.save()
        self.user.save()

        self.unit = Unit.objects.create(
            name="OOH",
            unit_type=self.unit_type,
            adzmart_hash="1234FG",
            unit_info={"key": "value"},
            user_id=self.user.id,
        )
        self.unit.save()

        self.cinema_unit = CinemaUnit.objects.create(
            cinema="Silverbird",
            location="Ikeja Mall",
            rate_per_spot="15000",
            state="Lagos",
            user_id=self.user.id,
        )
        self.cinema_unit.save()

    def test_upload_static_inventory_url_exists_at_correct_location(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get("/upload-static-inventory/")
        self.assertEqual(response.status_code, 200)

    def test_upload_cinema_inventory_url_exists_at_correct_location(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get("/upload-cinema-inventory/")
        self.assertEqual(response.status_code, 200)

    def test_upload_tv_inventory_url_exists_at_correct_location(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get("/upload-tv-inventory/")
        self.assertEqual(response.status_code, 200)

    def test_upload_radio_inventory_url_exists_at_correct_location(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get("/upload-radio-inventory/")
        self.assertEqual(response.status_code, 200)

    def test_upload_static_inventory_catalog_url_available_by_name(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_billboard_catalog"))
        self.assertEqual(response.status_code, 200)

    def test_upload_cinema_inventory_catalog_url_available_by_name(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_cinema_catalog"))
        self.assertEqual(response.status_code, 200)

    def test_upload_tv_catalog_url_available_by_name(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_tv_catalog"))
        self.assertEqual(response.status_code, 200)

    def test_upload_radio_catalog_url_available_by_name(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_radio_catalog"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_billboard_catalog"))
        self.assertTemplateUsed(response, "catalog/common/importexcel.html")

    def test_template_content(self):
        self.client.login(email="test@gmail.com", password="password")
        response = self.client.get(reverse("catalog:upload_billboard_catalog"))
        self.assertContains(
            response,
            '<button class="btn btn-primary" id="upload" type="submit">Upload Inventory</button>',
        )
        self.assertNotContains(response, "Not on the page")
