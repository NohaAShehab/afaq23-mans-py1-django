from django.db import models
from django.shortcuts import get_object_or_404, reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='posts/images', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_all_objects(cls):
        return cls.objects.all()

    @classmethod
    def get_specific_object(cls, id):
        return get_object_or_404(cls, pk=id)


    def get_image_url(self):
        return f"/media/{self.image}"

    @classmethod
    def delete_object(cls, id):
        obj = get_object_or_404(cls, pk=id)
        if obj:
            obj.delete()
            return True

    def get_delete_url(self):
        return reverse('posts.delete', args=[self.id])
    def get_edit_url(self):
        return reverse('posts.edit', args=[self.id])
