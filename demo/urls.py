from django.urls import path

from . import views
from .views import GetPhotos, GetUserAlbums, GetUsersList, UserAPI

urlpatterns =[
    path('albums',GetUserAlbums.as_view(),name="Albums"),
    path('get_photos', GetPhotos.as_view(), name='get_photos'),
    path('photos',views.PhotoList.as_view()),    
    path('user', UserAPI.as_view(), name='user'),
    path('users_list',GetUsersList.as_view())
]