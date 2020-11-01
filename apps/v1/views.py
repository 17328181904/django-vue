from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth.models import User,Group
from django.conf import settings
#django restframework
from rest_framework.response import Response
from  rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,generics
from rest_framework import permissions,status
from rest_framework import mixins
from rest_framework.renderers import JSONRenderer
import json
import requests
from .models import MapCity

# Create your views here.

from v1.serializers import MapCitySerializer


class IndexView(APIView):

    def __init__(self):
        super(APIView).__init__()
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0",
        }
    def get(self,request,*args,**kwargs):
        ip=request.META.get("REMOTE_ADDR")
        # query2 = request.GET.get("type")
        # query = request.META.get("HTTP_TYPE")
        data={
            "status":0,
            "data":"successe"
        }
        return Response(data,status=200)



# class BookInfoViewSet(APIView):
#     def get(self,request):
#         queryset = BookInfo.objects.all()
#         serializer_class = BookInfoSeriallizer(queryset)
#         print(serializer_class.data)
#         # print(serializer_class.data)
#         list = []
#         for i in serializer_class.data:
#             list.append(i)
#         return Response(list)

    # def get(self,request):
    #     return Response(serializer_class)
    # return Response("book")


#腾讯地图
class TenMap(APIView):
    def get_object(self, pk):

        try:
            name=pk[0:1]
            # result =MapCity.objects.filter(name=name)
            result = MapCity.objects.get(name=name)
            # for i in result:
            #     print(i.title_head)
            # return result[0]
            return result
        except MapCity.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        serializer = MapCitySerializer(city)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)




class MapList(generics.ListCreateAPIView):
    queryset = MapCity.objects.all()
    serializer_class = MapCitySerializer


# class MapList(generics.RetrieveAPIView):
#     queryset = MapCity.objects.all()
#     serializer_class = MapCitySerializer

# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)