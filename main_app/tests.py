from django.test import TestCase
from django.contrib.auth.models import User
from .models import Travel, Checklist

class TravelModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Travel.objects.create(
            name='Test Trip',
            country='Test Country',
            city='Test City',
            description='Test Description',
            user=user
        )

    def test_travel_creation(self):
        trip = Travel.objects.get(name='Test Trip')
        self.assertEqual(trip.country, 'Test Country')

class ChecklistModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username='testuser')
        Checklist.objects.create(
            name='Test Checklist',
            description='Test Desc',
            user=user
        )

    def test_checklist_creation(self):
        checklist = Checklist.objects.get(name='Test Checklist')
        self.assertEqual(checklist.description, 'Test Desc')
