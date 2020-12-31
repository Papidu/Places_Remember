from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.viewsets import ModelViewSet

from .models import RememberCards
from .serializers import RememberCardsSerializer


class RememberCardsViewSet(ModelViewSet):
    queryset = RememberCards.objects.all()
    serializer_class = RememberCardsSerializer


def welcome_windows(request):
    return render(request, "index.html")

