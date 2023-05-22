from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.shortcuts import get_object_or_404
from apps.DFM.models import Support, MediaBrief, MediaAdvisory

class SupportAPITestCase(APITestCase):
    def create_support_listing(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@gmail.com",
            "phone": "08906784972",
            "company_name": "Adzmart",
            "is_existing_customer": "true",
            "preferred_contact_method": "Email",
            "request_info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
        }
        response = self.client.post(reverse("DFM:support-listings"), data)
        return response


class TestListCreateSupport(SupportAPITestCase):

    def test_creates_support(self):
        response = self.create_support_listing()
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_not_create_support(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@gmail.com",
            "phone": "08906784972",
            "company_name": "Chevron",
            "is_existing_customer": "true",
        }
        response = self.client.post(reverse("DFM:support-listings"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestRetrieveUpdateDeleteSupport(SupportAPITestCase):
    def test_retrieve_support_listings(self):
        response = self.client.get(reverse("DFM:support-listings"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.create_support_listing()
        self.assertIsInstance(response.data["first_name"], str)

    def test_update_support_listing(self):
        response = self.create_support_listing()
        res = self.client.put(reverse("DFM:support-details", kwargs={"pk": response.data["id"]}), {
            "first_name": "Micheal",
            "last_name": "Smith",
            "email": "test@gmail.com",
            "phone": "08906784972",
            "company_name": "Adzmart",
            "is_existing_customer": "false",
            "preferred_contact_method": "Email",
            "request_info": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
        } )
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        updated_support = get_object_or_404(Support, pk=res.data["id"])

        self.assertEqual(updated_support.first_name, "Micheal")
        self.assertEqual(updated_support.is_existing_customer, False)


    def test_delete_support_listing(self):
        response = self.create_support_listing()
        prev_db_count = Support.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        res = self.client.delete(reverse("DFM:support-details", kwargs={"pk":response.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Support.objects.all().count(), 0)


class MediaBriefAPITestCase(APITestCase):
    def create_brief_listing(self):
        data = {
                "first_name":"John",
                "last_name": "Doe",
                "phone": "08906784972",
                "email" : "test@gmail.com",
                "company_name": "Adzmart",
                "is_existing_customer": "false",
                "preferred_contact_method": "Email",
                "media_type": "Radio",
                "campaign_details" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                "target_audience" : "Teenagers",
                "location" : "Lagos",
                "duration" : "6:00pm - 10:00pm every wednesday"
            }
        response = self.client.post(reverse("DFM:media-brief-listings"), data)
        return response


class TestListCreateMediaBrief(MediaBriefAPITestCase):

    def test_creates_media_brief(self):
        response = self.create_brief_listing()
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_not_create_support(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@gmail.com",
            "phone": "08906784972",
            "company_name": "Chevron",
            "is_existing_customer": "true",
        }
        response = self.client.post(reverse("DFM:media-brief-listings"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestRetrieveUpdateDeleteMediaBrief(MediaBriefAPITestCase):
    def test_retrieve_media_brief_listings(self):
        response = self.client.get(reverse("DFM:media-brief-listings"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.create_brief_listing()
        self.assertIsInstance(response.data["first_name"], str)

    def test_update_media_brief_listing(self):
        response = self.create_brief_listing()
        res = self.client.put(reverse("DFM:media-brief-details", kwargs={"pk": response.data["id"]}), 
        {
                "first_name":"Micheal",
                "last_name": "Doe",
                "phone": "08906784972",
                "email" : "test@gmail.com",
                "company_name": "Adzmart",
                "is_existing_customer": "false",
                "preferred_contact_method": "Email",
                "media_type": "Mobile",
                "campaign_details" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
                "target_audience" : "Teenagers",
                "location" : "Lagos",
                "duration" : "6:00pm - 10:00pm every wednesday"
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        updated_brief = get_object_or_404(MediaBrief, pk=res.data["id"])

        self.assertEqual(updated_brief.first_name, "Micheal")
        self.assertEqual(updated_brief.is_existing_customer, False)


    def test_delete_media_brief_listing(self):
        response = self.create_brief_listing()
        prev_db_count = MediaBrief.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        res = self.client.delete(reverse("DFM:media-brief-details", kwargs={"pk":response.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MediaBrief.objects.all().count(), 0)


class MediaAdvisoryAPITestCase(APITestCase):
    def create_advisory_listing(self):
        data = {
                "first_name":"John",
                "last_name": "Doe",
                "phone": "08906784972",
                "email": "test@gmail.com",
                "company_name": "Adzmart",
                "is_existing_customer": "true",
                "preferred_contact_method": "Phone",
                "support_type": "Media Advisory",
                "media_type" : "Mobile",
                "planned_budget" : "N200,000 - N500,000",
                "advertising_experience" : "I have no experience so far and only need information at first",
                "additional_info" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
            }
        response = self.client.post(reverse("DFM:media-advisory-listings"), data)
        return response


class TestListCreateMediaBrief(MediaAdvisoryAPITestCase):

    def test_creates_media_advisory(self):
        response = self.create_advisory_listing()
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_not_create_advisory(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@gmail.com",
            "phone": "08906784972",
            "company_name": "Chevron",
            "is_existing_customer": "true",
        }
        response = self.client.post(reverse("DFM:media-advisory-listings"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestRetrieveUpdateDeleteMediaAdvisory(MediaAdvisoryAPITestCase):
    def test_retrieve_media_advisory_listings(self):
        response = self.client.get(reverse("DFM:media-advisory-listings"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.create_advisory_listing()
        self.assertIsInstance(response.data["first_name"], str)

    def test_update_media_advisory_listing(self):
        response = self.create_advisory_listing()
        res = self.client.put(reverse("DFM:media-advisory-details", kwargs={"pk": response.data["id"]}), 
            {
                "first_name":"Micheal",
                "last_name": "Doe",
                "phone": "08906784972",
                "email": "test@gmail.com",
                "company_name": "Adzmart",
                "is_existing_customer": "true",
                "preferred_contact_method": "Phone",
                "support_type": "Media Advisory",
                "media_type" : "Radio",
                "planned_budget" : "N200,000 - N500,000",
                "advertising_experience" : "I have no experience so far and only need information at first",
                "additional_info" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
            })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        updated_advisory = get_object_or_404(MediaAdvisory, pk=res.data["id"])

        self.assertEqual(updated_advisory.first_name, "Micheal")
        self.assertEqual(updated_advisory.is_existing_customer, True)


    def test_delete_media_advisory_listing(self):
        response = self.create_advisory_listing()
        prev_db_count = MediaAdvisory.objects.all().count()

        self.assertGreater(prev_db_count, 0)
        self.assertEqual(prev_db_count, 1)

        res = self.client.delete(reverse("DFM:media-advisory-details", kwargs={"pk":response.data["id"]}))
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(MediaAdvisory.objects.all().count(), 0)
