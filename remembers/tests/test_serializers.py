import json

from django.contrib.auth.models import User
from django.test import TestCase

from remembers.models import RememberCards
from remembers.serializers import RememberCardsSerializer


class RememberCardsSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_dasha')
        self.remember_card1 = RememberCards.objects.create(location='New York', image='/img/sda', notes='dasdasdaahag', user=self.user)
        self.remember_card2 = RememberCards.objects.create(location='Yalta', image='/img/sda2', notes='dasdayyyyyyyy', user=self.user)

    def test_ok(self):
        serializer_data = RememberCardsSerializer([self.remember_card1, self.remember_card2], many=True).data
        expected_data = [
            {
            "id": self.remember_card1.id,
            "location": 'New York',
            "image": '/img/sda',
            "notes": 'dasdasdaahag',
            "user": 1,
            },
            {
            "id": self.remember_card2.id,
            "location": 'Yalta',
            "image": '/img/sda2',
            "notes": "dasdayyyyyyyy",
            "user": 1,
            },
        ]
        self.assertEqual(expected_data, serializer_data)
