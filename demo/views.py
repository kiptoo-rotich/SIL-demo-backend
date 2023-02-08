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

class GetUsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializer(users,many=True)
        return Response(serializers.data)

# Create Album view to post data
class AlbumList(APIView):
    def post(self, request):
        serializers = AlbumSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Pass user_id as a parameter for filtering albums
class GetUserAlbums(generics.ListAPIView):
    permission_classes=(permissions.AllowAny,)
    serializer_class = AlbumSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Album.objects.all()
        user_id = self.request.query_params.get('user_id')
        queryset = queryset.filter(user_id=user_id)
        return queryset


# Create Photo view to get and post data
class GetPhotos(generics.ListAPIView):
    permission_classes=(permissions.AllowAny,)
    serializer_class = PhotoSerializer
    http_method_names = ['get']

    def get_queryset(self):
        queryset = Album.objects.all()
        album_id = self.request.query_params.get('album_id')
        queryset = queryset.filter(album_id=album_id)
        return queryset

class PhotoList(APIView):
    def post(self, request):
        serializers = PhotoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)