from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Track(models.Model):
    name= models.CharField(max_length=100)
    image= models.ImageField(upload_to='tracks/images',  null=True )
    description  = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return f"{self.name}"

    @classmethod
    def get_all_tracks(cls):
        return cls.objects.all()

    def get_image_url(self):
        return  f"/media/{self.image}"

    @classmethod
    def get_specific_track(cls, id):
        return cls.objects.get(id=id)