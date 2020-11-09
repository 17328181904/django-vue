from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views
from django.conf.urls import url
from rest_framework import routers
from rest_framework.viewsets import generics




# router = DefaultRouter()
# router.register(r'maps', views.TenMapViewSet)
# urlpatterns = router.urls

map_list = views.TenMapViewSet.as_view({
    "get":"list"
})
get_city_id = views.TenMapViewSet.as_view({
    "get":"getCityById"
})

get_exact_address =views.TenMapViewSet.as_view({
    "get":"getExactAddress"
})
pois =views.TenMapViewSet.as_view({
    "get":"pois"
})


urlpatterns = [

    url(r'^cities/$',map_list,name="map_list"),
    url(r'^map/city/id/$',get_city_id,name="get_city_id"),
    url(r'^map/city/address/$',get_exact_address,name="get_exact_address"),
url(r'^pois/$',pois,name="pois"),

]