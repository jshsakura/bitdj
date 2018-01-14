from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.db.models import Min, Max
from django.shortcuts import get_object_or_404
from django.utils import timezone
from account.models import User

class Post(models.Model):
    #author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    email = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    #post_img = models.CharField(max_length=500,blank=True, null=True,default="static/assets/images/gl-11.jpg")
    #post_img = models.ImageField(null=True, blank=True, upload_to="blog/%Y/%m/%d")
    image = models.ImageField(upload_to='blog/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, blank=True, null=True, default="")
    text = models.TextField()
    hit = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    #승인된 댓글만 보기
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    #다음글 가져오기
    def get_next_object(self):
        try:
            id = Post.objects.filter(id__gt=self.id).order_by("id")[0:1].get().id
            next_object = get_object_or_404(Post, pk=id)
        except Post.DoesNotExist:
            id = Post.objects.aggregate(Min("id"))['id__min']
            next_object = get_object_or_404(Post, pk=id)
        return next_object

    # 이전글 가져오기
    def get_prev_object(self):
        try:
            id = Post.objects.filter(id__lt=self.id).order_by("-id")[0:1].get().id
            prev_object = get_object_or_404(Post, pk=id)
        except Post.DoesNotExist:
            id = Post.objects.aggregate(Max("id"))['id__max']
            prev_object = get_object_or_404(Post, pk=id)
        return prev_object


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    image = models.ImageField(upload_to='contact/%Y/%m/%d', blank=True, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE,)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200, blank=True, null=True, default="",)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True,)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text