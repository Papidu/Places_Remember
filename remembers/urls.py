from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from remembers.models import RememberCards
from remembers.views import RememberCardsViewSet, OwnerCardsViewSet, HomePageView, welcome_windows, test, create_model, \
    MapaLayer
from djgeojson.views import GeoJSONLayerView
router = SimpleRouter()

router.register(r'api/aremembercards', RememberCardsViewSet)
router.register(r'api/ownercards', OwnerCardsViewSet, basename='ownercards')


urlpatterns = [
    url(r'map', HomePageView.as_view(), name='home'),
    url(r'^data/$', MapaLayer.as_view(), name='data'),
    url(r'dashboard', welcome_windows, name='dashboard'),
    url(r'create_place', create_model, name='create_place'),
    url(r'test', test, name='test')
]

urlpatterns += router.urls
