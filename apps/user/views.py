from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from .models import Ad,Uses
from .serializer import UserSeriallizer
# Create your views here.
import logging


log = logging.getLogger("log")

# class Ad(generics.ListCreateAPIView):
#     queryset = Ad.objects.all()
#     serializer_class =AdSeriallizer


class UserInfo(ViewSet):

    def list(self,request):
        user_id = request.GET.get("user_id")

        if not user_id or  user_id.isdigit()==False:
            log.error("user_id is must number")
            return Response({"errmsg":"user_id is must number"})

        try:
            queryset = Uses.objects.get(user_id=user_id)
            serializer = UserSeriallizer(queryset)
            return  Response(serializer.data)
        except Exception as e:
            log.info("user_id is not find")
            return  Response({"errmsg":"通过id 获取 用户信息失败"})





