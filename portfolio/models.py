from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.core.files.images import ImageFile
from django.db.models import ImageField
from django.utils.safestring import mark_safe


class Portfolio(models.Model):
    email = models.ForeignKey(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='portfolio/%Y/%m/%d',null=True)
    filtered_image = models.ImageField(upload_to='portfolio/%Y/%m/%d/filtered', blank=True, null=True)

    tag = models.CharField(max_length=200,blank=True, null=True)
    url = models.CharField(max_length=1000,blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)

    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk': self.pk})
        return url

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):  # image 삭제 함수 추가
        self.image.delete();
        super(Portfolio, self).delete(*args, **kwargs)

    def image_tag(self):
        return mark_safe('<img src="/%s" />' % (self.image))

    image_tag.short_description = 'Image'
