from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Person

class PersonApiTests(APITestCase):
    def setUp(self):
        self.person = Person.objects.create(name='John', age=30)

    def test_get_person_by_name(self):
        url = reverse('person-by-name-retrieve-update-destroy', args=[self.person.name])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John')
        self.assertEqual(response.data['age'], 30)

