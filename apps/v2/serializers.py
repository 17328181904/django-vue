from rest_framework import serializers
from .models import Head_content


class HeadContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Head_content
        fields="__all__"