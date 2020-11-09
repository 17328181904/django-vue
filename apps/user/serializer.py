from .models import Uses
from rest_framework.serializers import ModelSerializer


class UserSeriallizer(ModelSerializer):


    class Meta:
        model = Uses
        fields="__all__"

