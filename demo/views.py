from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Album, Photo
from .serializers import (AlbumSerializer, PhotoSerializer, RegisterSerializer,
                          UserSerializer)


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

# Create Album view to get and post data
class AlbumList(APIView):
    def get(self, request):
        albums = Album.objects.all()
        serializers = AlbumSerializer(albums,many=True)
        return Response(serializers.data)


    def post(self, request):
        serializers = AlbumSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Create Photo view to get and post data
class PhotoList(APIView):
    def get(self, request):
        photos = Photo.objects.all()
        serializers = PhotoSerializer(photos,many=True)
        return Response(serializers.data)


    def post(self, request):
        serializers = PhotoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)