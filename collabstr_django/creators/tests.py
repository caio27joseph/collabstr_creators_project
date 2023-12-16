from django.test import TestCase
from django.urls import reverse
from .models import Creator, Content
from rest_framework.test import APIClient


class CreatorCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.creator = Creator.objects.create(
            name="John Doe", username="johndoe", rating=4.5, platform="IG"
        )
        self.list_create_url = reverse("creator_list_create")
        self.detail_url = reverse("creator_retrieve_update_delete", args=[self.creator.id])

    def test_creator_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.creator.name)

    def test_creator_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.creator.name)

    def test_creator_create(self):
        response = self.client.post(
            self.list_create_url,
            {"name": "New Creator", "username": "newcreator", "rating": 4.2, "platform": "TT"},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Creator.objects.count(), 2)
        self.assertEqual(Creator.objects.last().name, "New Creator")

    def test_creator_update(self):
        updated_data = {
            "name": "John Updated",
            "username": "johnupdated",
            "rating": 4.8,
            "platform": "TT",
        }
        response = self.client.put(
            self.detail_url,
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        updated_creator = Creator.objects.get(id=self.creator.id)
        self.assertEqual(updated_creator.name, updated_data["name"])
        self.assertEqual(updated_creator.username, updated_data["username"])
        self.assertEqual(float(updated_creator.rating), updated_data["rating"])
        self.assertEqual(updated_creator.platform, updated_data["platform"])

    def test_creator_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)


class ContentCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.creator = Creator.objects.create(
            name="Jane Doe", username="janedoe", rating=4.7, platform="TT"
        )
        self.content = Content.objects.create(
            creator=self.creator, url="http://example.com/content.jpg"
        )
        self.list_create_url = reverse("content_list_create", args=[self.creator.id])
        self.detail_url = reverse(
            "content_retrieve_update_delete", args=[self.creator.id, self.content.id]
        )

    def test_content_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.content.url)

    def test_content_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.content.url)

    def test_content_create(self):
        response = self.client.post(
            self.list_create_url,
            {"creator": self.creator.id, "url": "http://example.com/new_content.jpg"},
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Content.objects.count(), 2)
        self.assertEqual(Content.objects.last().url, "http://example.com/new_content.jpg")

    def test_content_update(self):
        updated_data = {
            "creator": self.creator.id,
            "url": "http://example.com/updated_content.jpg",
        }
        response = self.client.put(
            self.detail_url,
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        updated_content = Content.objects.get(id=self.content.id)
        self.assertEqual(updated_content.url, updated_data["url"])

    def test_content_delete(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
