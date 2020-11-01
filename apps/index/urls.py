from django.urls import path
from . import views

urlpatterns=[
    path(r'',views.welcome),
    path(r'index',views.index)
]