from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import RememberCards
from .serializers import RememberCardsSerializer


class RememberCardsViewSet(ModelViewSet):
    queryset = RememberCards.objects.all()
    serializer_class = RememberCardsSerializer

