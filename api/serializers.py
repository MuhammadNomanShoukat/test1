from django.contrib.auth.admin import User
from .models import Profile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.core import exceptions

# ===================================================== User Seriializer class =====================================
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
        ]

    """ making password from password field data to login with local username """
    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password']=make_password(validated_data['password'])
            user = User.objects.create(**validated_data)
            return user

# =========================================================== Profile Serializers Class ===============================
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'user',
            'cnic',
            'address',
            'phone',
        ]
