from django.conf.urls import url
from django.urls import path

from . import views


user = views.UserInfo.as_view({
    "get":"list"
})

urlpatterns=[
    url(r'^userinfo/$',user,name="user")

]