from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from remembers.views import RememberCardsViewSet, OwnerCardsViewSet

router = SimpleRouter()

router.register(r'api/aremembercards', RememberCardsViewSet)
router.register(r'api/ownercards', OwnerCardsViewSet, basename='ownercards')


urlpatterns = [

]

urlpatterns += router.urls
