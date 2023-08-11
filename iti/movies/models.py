from django.db import models
from django.shortcuts import  get_object_or_404, reverse
from topics.models import Topic
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    no_views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='movies/images', null=True, blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    def get_image_url(self):
        return f"/media/{self.image}"

    @classmethod
    def get_specific_object(cls, id):
        return get_object_or_404(cls, pk=id)

    def get_edit_url(self):
        return reverse('movies.edit', args=[self.id])

    def get_delete_url(self):
        return reverse('movies.delete', args=[self.id])

    def get_show_url(self):
        return reverse('movies.show', args=[self.id])