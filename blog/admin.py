from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

from .models import Post
admin.site.register(Post)

#@admin.register(Post)
#class PostAdmin(admin.ModelAdmin):
#    list_display = ['id', 'author','title', 'created_date', 'published_date' ]
#    actions = ['make_published', 'make_draft']

    # 글자수 컬럼 추가
    #def content_size(self, post):
    #    return mark_safe('<u>{}</u>글자'.format(len(post.content)))
    #content_size.short_description = '글자수'

    # admin action 추가
#    def make_published(self, request, queryset):
#        updated_count = queryset.update(published_date=timezone.now()) #queryset.update
#        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count)) #django message framework 활용
#    make_published.short_description = '지정 포스팅을 Published 상태로 변경'

#    def make_draft(self, request, queryset):
#        updated_count = queryset.update(published_date='') #queryset.update
#        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count)) #django message framework 활용
#    make_draft.short_description = '지정 포스팅을 draft 상태로 변경'