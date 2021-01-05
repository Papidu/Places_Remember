from django.contrib import admin
from django.contrib.gis import admin as admin_gis
from remembers.models import RememberCards
from  leaflet.admin import LeafletGeoAdmin
# admin.site.register(RememberCards, admin_gis.OSMGeoAdmin)

admin.site.register(RememberCards, LeafletGeoAdmin)
