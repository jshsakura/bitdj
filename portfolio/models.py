from django.conf import settings
from django.db import models
from django.utils import timezone


class Portfolio(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)

    title = models.CharField(max_length=200)
    text = models.TextField()
    img_src = models.CharField(max_length=500,blank=True, null=True)
    tag = models.CharField(max_length=200,blank=True, null=True)
    url = models.CharField(max_length=1000,blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
