from rest_framework import serializers
from v1.models import MapCity
from django.contrib.auth.models import User,Group
from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import detail_route


class MapCitySerializer(serializers.ModelSerializer):



    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
    #     """
    #     return MapCity.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     # instance.code = validated_data.get('code', instance.code)
    #     # instance.linenos = validated_data.get('linenos', instance.linenos)
    #     # instance.language = validated_data.get('language', instance.language)
    #     # instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
    class Meta:
        model = MapCity

        fields = ["title_head","name","id"]