from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Item


class ItemTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_item = Item.objects.create(
            name="rake",
            creator=testuser1,
            description="Better for collecting leaves than a shovel.",
        )
        test_item.save()

    def setUp(self):
        self.client.login(username="testuser1", password="pass")

    def test_item_model(self):
        item = Item.objects.get(id=1)
        actual_creator = str(item.creator)
        actual_name = str(item.name)
        actual_description = str(item.description)
        self.assertEqual(actual_creator, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel."
        )

    def test_get_item_list(self):
        url = reverse("item_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        items = response.data
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "rake")

    def test_get_item_by_id(self):
        url = reverse("item_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = response.data
        self.assertEqual(item["name"], "rake")

    def test_create_item(self):
        url = reverse("item_list")
        data = {"creator": 1, "name": "spoon", "description": "good for cereal and soup"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        items = Item.objects.all()
        self.assertEqual(len(items), 2)
        self.assertEqual(Item.objects.get(id=2).name, "spoon")

    def test_update_item(self):
        url = reverse("item_detail", args=(1,))
        data = {
            "creator": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, data["name"])
        self.assertEqual(item.creator.id, data["creator"])
        self.assertEqual(item.description, data["description"])

    def test_delete_item(self):
        url = reverse("item_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        items = Item.objects.all()
        self.assertEqual(len(items), 0)

    # added to template
    def test_authentication_required(self):
        self.client.logout()
        url = reverse("item_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_FORBIDDEN)
