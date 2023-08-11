from django.db import models
from django.shortcuts import reverse, get_object_or_404
# Create your models here.


class Topic (models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='topics/images',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    def get_logo_url(self):
        return f"/media/{self.logo}"

    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)

    def get_edit_url(self):
        return reverse('topics.edit', args=[self.id])