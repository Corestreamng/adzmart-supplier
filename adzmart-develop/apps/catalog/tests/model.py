from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from apps.catalog.admin import UnitAdmin
from apps.catalog.models import (
    UnitType,
    Unit,
    RadioUnit,
    TVUnit,
    BillboardImage,
    CinemaUnit,
    PrintUnit,
    SpecialOffers
)
from apps.authentication.models import User
from django.conf import settings
from datetime import datetime
import requests
import os


class RequestObj(object):
    def __init__(self, deleted_at=datetime.now()):
        self.deleted_at = deleted_at


class TestCatalogModel(TestCase):
    def test_unit_type_model_str(self):
        name = UnitType.objects.create(name="Billboard")
        description = UnitType.objects.create(description="Owned by Radio Nigeria")

        self.assertEquals(str(name), "Billboard")

    def test_unit_model_str(self):
        unit_type = UnitType(name="Radio")
        user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )

        user.save()
        unit_type.save()

        unit = Unit.objects.create(
            name="OOH",
            unit_type=unit_type,
            adzmart_hash="1234FG",
            unit_info={"key": "value"},
            user_id=user.id,
        )
        unit.save()

        record = Unit.objects.get(user=unit.user_id)
        self.assertEquals(str(record.unit_type.name), "Radio")
        self.assertEquals(str(unit.name), "OOH")


class TestRadioCatalogModel(TestCase):
    def setUp(self):
        self.user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.save()

    def test_radio_model_str(self):
        radio_unit = RadioUnit(user=self.user, Vendor_Name="Kiss FM")
        radio_unit.save()
        record = RadioUnit.objects.get(user=self.user)
        self.assertEquals(str(record.Vendor_Name), "Kiss FM")


class TestTVCatalogModel(TestCase):
    def setUp(self):
        self.user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.save()

    def test_tv_model_str(self):
        tv_unit = TVUnit(user=self.user, Vendor_Name="Africa Magic Epic")
        tv_unit.save()
        record = TVUnit.objects.get(user=self.user)
        self.assertEquals(str(record.Vendor_Name), "Africa Magic Epic")


class TestCinemaCatalogModel(TestCase):
    def setUp(self):
        self.user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.save()

    def test_cinema_unit_type_model_str(self):
        cinema_unit = CinemaUnit(
            user=self.user,
            cinema="Silverbird",
            location="Ikeja Mall",
            rate_per_spot="15000",
            state="Lagos",
        )
        cinema_unit.save()
        record = CinemaUnit.objects.get(user=self.user)
        self.assertEquals(str(record.cinema), "Silverbird")


class TestBillboardImageModel(TestCase):
    def test_billboard_image_model_str(self):
        billboard_image = BillboardImage(
            image="REFXX_image1.jpg", reference_id="REFXX", image_public_id="89ysbyiwr2"
        )
        billboard_image.save()
        image_record = BillboardImage.objects.get(id=1)
        self.assertEquals(str(image_record.image), 'REFXX_image1')

class TestSpecialOffersModel(TestCase):
    def setUp(self):
        self.user = User(email='test@gmail.com', password='password', first_name='firstname', last_name='last_name')
        self.user.save()

    def test_special_offers_model_str(self):
        special_offer = SpecialOffers(title="SEO", description="Test", user=self.user, services="Test", rate=145.34)
        special_offer.save()
        record = SpecialOffers.objects.get(id=1)
        self.assertEquals(record.title, 'SEO')


class TestPrintCatalogModel(TestCase):
    def setUp(self):
        self.user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        self.user.save()

    def test_print_model_str(self):
        print_unit = PrintUnit(
            user=self.user,
            coverage="National",
            publisher="Punch",
            title="Daily Punch",
            type="Color",
            size="Full Page",
            position="Classified Advert",
            rate=56.90,
            agency_discount=45.9,
            amount=43.1,
            vat=7.89,
            total=67.90
            
        )
        print_unit.save()
        record = PrintUnit.objects.get(user=self.user)
        self.assertEquals(str(record.publisher), "Punch")
