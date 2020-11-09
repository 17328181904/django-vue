from django.shortcuts import render

from rest_framework import viewsets,generics
from rest_framework.response import Response

from .models import Head_content
from .serializers import HeadContentSerializer
# Create your views here.


class HeadTabarViewSet(viewsets.ViewSet):
    def list(self, request):

        queryset = Head_content.objects.filter(is_in_serving=1)

        serializer = HeadContentSerializer(queryset,many=True)

        return Response(serializer.data)
