from django.urls import path

from . import views
from .views import UserAPI

urlpatterns =[
    path('albums',views.AlbumList.as_view()),
    path('photos',views.PhotoList.as_view()),    
    path('user', UserAPI.as_view(), name='user'),
]