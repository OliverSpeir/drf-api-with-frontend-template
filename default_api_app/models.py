from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Item(models.Model):
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.TextField(default='name')
    description = models.TextField(default='description')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(default='https://i.imgur.com/yFvRMHe.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])