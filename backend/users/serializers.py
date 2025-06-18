from dj_rest_auth.serializers import UserDetailsSerializer
from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username')