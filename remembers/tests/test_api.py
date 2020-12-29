import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from remembers.models import RememberCards
from remembers.serializers import RememberCardsSerializer


class RememberCardsViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='test_dasha')
        self.remember_card1 = RememberCards.objects.create(location='New York', image='/img/sda', notes='dasdasdaahag', user=self.user)
        self.remember_card2 = RememberCards.objects.create(location='Yalta', image='/img/sda2', notes='dasdayyyyyyyy', user=self.user)

    def test_get(self):
        url = reverse('remembercards-list')
        self.client.force_login(self.user)
        serializer_data = RememberCardsSerializer([self.remember_card1, self.remember_card2], many=True).data
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, RememberCards.objects.all().count())
        url = reverse('remembercards-list')
        expected_data = {
                    "location": 'Moscow',
                    "image": "/img/sda",
                    "notes": "Lololololo",
                    "user": 1,
                }
        json_data = json.dumps(expected_data)
        self.client.force_login(self.user)
        response = self.client.post(url, data=json_data, content_type='application/json')
        serializer_data = RememberCardsSerializer([self.remember_card1, self.remember_card2], many=True).data
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, RememberCards.objects.all().count())
