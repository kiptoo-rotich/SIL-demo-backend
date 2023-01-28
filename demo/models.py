from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField


class Album(models.Model):
    title = CharField(max_length=50)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = CharField(max_length=50)
    image_url = CharField(max_length=200)
    album_id = models.ForeignKey(Album,on_delete=models.CASCADE)

    def __str__(self):
        return self.title