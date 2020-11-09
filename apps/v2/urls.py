from  django.conf.urls import url
from .views import HeadTabarViewSet


head_list = HeadTabarViewSet.as_view({
    "get":"list"
})

urlpatterns=[
    url(r"^index_entry/$",head_list,name="head_list")
]