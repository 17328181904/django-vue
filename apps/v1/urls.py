from django.urls import path,include
from . import views
from django.conf.urls import url
from rest_framework import routers
from rest_framework.viewsets import generics






# user_list = UserSerializer.as_view({
#
# })
# router = routers.DefaultRouter()
# router.register(r'v1/users', views.UserViewSet)
# router.register(r'v1/groups', views.GroupViewSet)
# router.register(r'v1/book', views.BookInfoViewSet)
# router.register(r'v1/map', views.MapList)
urlpatterns = [
    url(r'^v1/city/(?P<pk>[a-zA-Z]+)/$',views.TenMap.as_view()),
    url(r'^v1/map/city',views.MapList.as_view()),
    url(r'^v1/map/city/<?P<pk>[a-zA-Z]*/$>',views.MapList.as_view()),
]