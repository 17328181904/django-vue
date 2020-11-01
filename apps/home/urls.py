from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views


# router = routers.DefaultRouter()

# router.register(r'users', views.UserViewSet)
# router.register(r'group',views.GroupViewSet)
urlpatterns=[
    # path(r'',views.welcome),
    # url(r'^',include(router.urls)),

    # url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'index/(?P<pk>[0-9]+)/$',views.IndexDetail.as_view()),
    url(r'^index/$',views.IndexViewList.as_view()),

    # path(r'index',views.index)
]