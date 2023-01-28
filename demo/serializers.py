from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Album, Photo


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','first_name','last_name')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], 
            email=validated_data['email'], 
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])

        return user

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model=Album
        fields='__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Photo
        fields='__all__'