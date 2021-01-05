from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import RememberCards
from .serializers import RememberCardsSerializer


class RememberCardsViewSet(ModelViewSet):
    queryset = RememberCards.objects.all()
    serializer_class = RememberCardsSerializer


class OwnerCardsViewSet(ModelViewSet):
    serializer_class = RememberCardsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RememberCards.objects.filter(user=self.request.user)


def welcome_windows(request):
    return render(request, "index.html")


def auth(request):
    return render(request, 'auth.html')


