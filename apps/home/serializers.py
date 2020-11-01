from rest_framework import serializers
from .models import Content, Snippet
from django.contrib.auth.models import User,Group
from rest_framework.viewsets import ModelViewSet

# from rest_framework.decorators import detail_route




class IndexSeriallizer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # def create(self, validated_data):
    #     """
    #     根据提供的验证过的数据创建并返回一个新的`Snippet`实例。
    #     """
    #     return Content.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     根据提供的验证过的数据更新和返回一个已经存在的`Snippet`实例。
    #     """
    #     instance.btitle = validated_data.get('btitle', instance.title)
    #     instance.bread = validated_data.get('bread', instance.code)
    #     instance.bcomment = validated_data.get('bcomment', instance.linenos)
    #     instance.save()
    #     return instance

    class Meta:
        model = Content
        fields="__all__"




class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippet = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields=("id","username","snippet")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields=("id","title","code","linenos","language","style","owner")