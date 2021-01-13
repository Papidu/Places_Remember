from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .forms import RememberForm
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
    return render(request, "remembers/add_remembers.html")


def test(request):
    data = RememberCards.objects.all()
    return render(request, "index.html", {'data': data, 'user': request.user})


def create_model(request):
    form = RememberForm()

    data = {
        "form": form,
    }
    return render(request, "index.html", data)


def auth(request):
    return render(request, 'auth.html')

#########

class HomePageView(TemplateView):
    template_name = 'home.html'


class MapaLayer(GeoJSONLayerView):
    model = RememberCards

