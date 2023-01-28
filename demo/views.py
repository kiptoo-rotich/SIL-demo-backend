from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializers = UserSerializer(users,many=True)
        return Response(serializers.data)