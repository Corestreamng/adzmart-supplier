from django.test import TestCase
from django.http import HttpRequest
from django.core.exceptions import ValidationError
from django.urls import reverse
from django import forms
from apps.catalog.forms import (
    UnitForm,
    RadioUnitForm,
    TVUnitForm,
    BillboardImageForm,
    CinemaUnitForm,
    SpecialOffersForm,
    PrintUnitForm,
)
from apps.authentication.models import User
from apps.authentication.form import AddStaffForm

import cloudinary
from cloudinary.forms import CloudinaryJsFileField
from cloudinary.forms import CloudinaryFileField
from cloudinary import CloudinaryResource
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.catalog.tests.helpers_test import (
    SUFFIX,
    TEST_IMAGE,
    TEST_IMAGE_H,
    TEST_IMAGE_W,
)
from mock import mock

API_TEST_ID = "cloudinary_test_{}".format(SUFFIX)


class TestAddStaffForms(TestCase):
    def test_add_staff_user_form(self):
        form = AddStaffForm(
            data={
                "email": "email@gmail.com",
                "first_name": "Tola",
                "last_name": "Abiodun",
                "phone_no": 2323989823,
            }
        )

        self.assertTrue(form.is_valid())
        self.assertEquals(form.clean_email(), form.cleaned_data["email"].lower())

    def test_add_staff_user_no_data(self):
        form = AddStaffForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_empty_form(self):
        form = AddStaffForm()
        self.assertIn("email", form.fields)
        self.assertIn("first_name", form.fields)

    def test_email_already_exits_on_staff_creation(self):
        user = User(
            email="test@gmail.com",
            password="password",
            first_name="firstname",
            last_name="last_name",
        )
        user.save()

        request = HttpRequest()
        request.POST = {
            "email": user.email,
            "first_name": "Tola",
            "last_name": "Joey",
            "phone_no": 789378734,
        }
        form = AddStaffForm(request.POST)
        self.assertTrue(form.has_error("email"))
        self.assertIn(
            "The invitation process could not be completed as email already exists.",
            form.errors["email"],
        )

    def test_new_staff_user_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            "email": "email@gmail.com",
            "first_name": "Tola",
            "last_name": "Joey",
            "phone_no": 789378734,
        }
        form = AddStaffForm(request.POST)
        response = self.client.post(
            reverse("authentication:add_staff_user"), request.POST
        )
        self.assertEqual(response.status_code, 302)


class TestBillboardUnitForm(TestCase):
    def test_add_billboard_unit_form(self):
        form = UnitForm(
            data={
                "longitude": 9.00,
                "latitude": 8.780,
                "name": "Billboard",
                "description": "Owned by Coca-cola",
                "facing": "NW",
                "district": "Ikeja",
            }
        )

        self.assertTrue(form.is_valid())

    def test_add_billboard_unit_no_data(self):
        form = UnitForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    def test_new_billboard_unit_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            "longitude": 9.00,
            "latitude": 8.780,
            "name": "Billboard",
            "description": "Owned by Coca-cola",
            "facing": "NW",
            "district": "Ikeja",
        }
        form = UnitForm(request.POST)
        response = self.client.post(
            reverse("catalog:load_billboard_catalog"), request.POST
        )
        self.assertEqual(response.status_code, 302)


class TestTVUnitForm(TestCase):
    def test_add_tv_unit_form(self):
        form = TVUnitForm(
            data={
                "Mp_Code": 1232,
                "Vendor_Name": "MultiChoice",
                "Corporate_Name": "Multichoice",
                "Station_Name": "Multichoice",
                "State": "Lagos",
                "Media_Type": "TV",
                "Time": "6:00-7.00pm",
                "Rate_Desc": "25",
                "Duration": "10secs",
                "Card_Rate": 25,
                "Nego_Rate": 10,
                "Card_VD": 10,
                "Nego_VD": 10,
                "Card_SC": 10,
                "Nego_SC": 10,
                "Add_VD": 10,
                "SP_Disc": 10,
                "Agency": 10,
                "VAT": 7.5,
            }
        )

        self.assertTrue(form.is_valid())

    def test_add_tv_unit_no_data(self):
        form = TVUnitForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 16)

    def test_new_tv_unit_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            "Mp_Code": 1232,
            "Vendor_Name": "MultiChoice",
            "Corporate_Name": "Multichoice",
            "Station_Name": "Multichoice",
            "State": "Lagos",
            "Media_Type": "TV",
            "Time": "6:00-7.00pm",
            "Rate_Desc": "25",
            "Duration": "10secs",
            "Card_Rate": 25,
            "Nego_Rate": 10,
            "Card_VD": 10,
            "Nego_VD": 10,
            "Card_SC": 10,
            "Nego_SC": 10,
            "Add_VD": 10,
            "SP_Disc": 10,
            "Agency": 10,
            "VAT": 7.5,
        }
        form = TVUnitForm(request.POST)
        response = self.client.post(reverse("catalog:load_tv_catalog"), request.POST)
        self.assertEqual(response.status_code, 302)


class TestRadioUnitForm(TestCase):
    def test_add_radio_unit_form(self):
        form = TVUnitForm(
            data={
                "Mp_Code": 1232,
                "Vendor_Name": "MultiChoice",
                "Corporate_Name": "Multichoice",
                "Station_Name": "Multichoice",
                "State": "Lagos",
                "Media_Type": "TV",
                "Time": "6:00-7.00pm",
                "Rate_Desc": "25",
                "Duration": "10secs",
                "Card_Rate": 25,
                "Nego_Rate": 10,
                "Card_VD": 10,
                "Nego_VD": 10,
                "Card_SC": 10,
                "Nego_SC": 10,
                "Add_VD": 10,
                "SP_Disc": 10,
                "Agency": 10,
                "VAT": 7.5,
            }
        )

        self.assertTrue(form.is_valid())

    def test_add_tv_unit_no_data(self):
        form = RadioUnitForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 16)

    def test_new_radio_unit_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            "Mp_Code": 1232,
            "Vendor_Name": "MultiChoice",
            "Corporate_Name": "Multichoice",
            "Station_Name": "Multichoice",
            "State": "Lagos",
            "Media_Type": "TV",
            "Time": "6:00-7.00pm",
            "Rate_Desc": "25",
            "Duration": "10secs",
            "Card_Rate": 25,
            "Nego_Rate": 10,
            "Card_VD": 10,
            "Nego_VD": 10,
            "Card_SC": 10,
            "Nego_SC": 10,
            "Add_VD": 10,
            "SP_Disc": 10,
            "Agency": 10,
            "VAT": 7.5,
        }
        form = RadioUnitForm(request.POST)
        response = self.client.post(reverse("catalog:load_radio_catalog"), request.POST)
        self.assertEqual(response.status_code, 302)


class TestCinemaUnitForm(TestCase):
    def test_add_cinema_unit_form(self):
        form = CinemaUnitForm(
            data={
                "cinema": "Silverbird",
                "location": "Ikeja Mall",
                "state": "Lagos",
                "rate_per_spot": "15000",
            }
        )

        self.assertTrue(form.is_valid())

    def test_add_cinema_unit_no_data(self):
        form = CinemaUnitForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_new_cinema_unit_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            "cinema": "Silverbird",
            "location": "Ikeja Mall",
            "state": "Lagos",
            "rate_per_hour": "15000",
        }
        form = CinemaUnitForm(request.POST)
        response = self.client.post(
            reverse("catalog:load_cinema_catalog"), request.POST
        )
        self.assertEqual(response.status_code, 302)


class CloudinaryJsTestFileForm(forms.Form):
    js_file_field = CloudinaryJsFileField(
        attrs={"style": "margin-top: 30px"},
        options={
            "tags": "directly_uploaded",
            "crop": "limit",
            "width": 1000,
            "height": 1000,
            "eager": [{"crop": "fill", "width": 150, "height": 100}],
        },
    )


class TestBillboardImageForm(TestCase):
    def setUp(self):
        self.test_file = SimpleUploadedFile(TEST_IMAGE, b"content")

    def test_file_field(self):
        cff_no_auto_save = CloudinaryFileField(autosave=False)
        res = cff_no_auto_save.to_python(None)
        self.assertIsNone(res)
        # without auto_save File is untouched
        res = cff_no_auto_save.to_python(self.test_file)
        self.assertIsInstance(res, SimpleUploadedFile)

        # when auto_save is used, resource is uploaded to Cloudinary and CloudinaryResource is returned
        cff_auto_save = CloudinaryFileField(
            autosave=True, options={"public_id": API_TEST_ID}
        )
        mocked_resource = cloudinary.CloudinaryResource(
            metadata={"width": TEST_IMAGE_W, "height": TEST_IMAGE_H},
            type="upload",
            public_id=API_TEST_ID,
            resource_type="image",
        )

        with mock.patch(
            "cloudinary.uploader.upload_image", return_value=mocked_resource
        ) as upload_mock:
            res = cff_auto_save.to_python(self.test_file)

        self.assertTrue(upload_mock.called)
        self.assertIsInstance(res, CloudinaryResource)
        self.assertEqual(API_TEST_ID, res.public_id)

    def test_js_file_field(self):
        js_file_form = CloudinaryJsTestFileForm()

        rendered_form = js_file_form.as_p()

        self.assertIn("margin-top: 30px", rendered_form)
        self.assertIn("directly_uploaded", rendered_form)
        self.assertIn("c_fill,h_100,w_150", rendered_form)
        self.assertIn("c_limit,h_1000,w_1000", rendered_form)

    def tearDown(self):
        pass


class TestSpecialOffersForm(TestCase):
    def test_add_special_offer_no_data(self):
        form = SpecialOffersForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

    def test_new_special_offer_created_redirect(self):
        request = HttpRequest()
        request.POST = {
            'title': "SEO",
            'description': "Test",
            'services': "Test",
            'rate': 145.34,
        }
        form = SpecialOffersForm(request.POST)
        response = self.client.post(
        reverse("catalog:load_special_offers"), request.POST)


class TestPrintUnitForm(TestCase):
    def test_add_print_unit_form(self):
        form = PrintUnitForm(
            data={
                "coverage": "National",
                "publisher": "Punch",
                "title": "Daily Punch",
                "type": "Color",
                "size": "Full page",
                "position": "Special position",
                "rate":4.56,
                "agency_discount":45.3,
                "amount": 23.54,
                "vat":45.64,
                "total": 234.54
            }
        )

        self.assertTrue(form.is_valid())

    def test_add_print_unit_no_data(self):
        form = PrintUnitForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 11)

    def test_new_print_unit_created_redirect(self):
        request = HttpRequest()
        request.POST = {
                "coverage": "National",
                "publisher": "Puch",
                "title": "Daily Punch",
                "type": "Color",
                "size": "Full page",
                "position": "Special position",
                "rate":4.567,
                "agency_discount":45.3,
                "amount": 23.54,
                "vat":45.64,
                "total": 234.54
            }
        form = PrintUnitForm(request.POST)
        response = self.client.post(
            reverse("catalog:load_print_catalog"), request.POST
        )
        self.assertEqual(response.status_code, 302)
