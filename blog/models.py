from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    post_img = models.CharField(max_length=500,blank=True, null=True,default="static/assets/images/gl-11.jpg")
    #post_img = models.ImageField(null=True, blank=True, upload_to="blog/%Y/%m/%d")
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, blank=True, null=True, default="")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)



