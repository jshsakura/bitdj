from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils import timezone

from .models import Post
#admin.site.register(Post.ModelAdmin);

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'title','tag', 'text_size', 'created_date','published_date', ]
    list_display_links = ['id', 'title']
    actions = ['make_published', 'make_draft']

    #admin action 추가
    # 글자수 컬럼 추가
    def text_size(self, post):
        return mark_safe('<u>{}</u> 글자'.format(len(post.text)))
        text_size.short_description = '글자수'

    def make_published(self, request, queryset):
        updated_count = queryset.update(published_date=timezone.now())  # queryset.update
        self.message_user(request, '{}건의 포스팅을 Published 상태로 변경'.format(updated_count))  # django message framework 활용

    make_published.short_description = '선택한 포스팅을 공개 상태로 변경'

    def make_draft(self, request, queryset):
        updated_count = queryset.update(published_date='')  # queryset.update
        self.message_user(request, '{}건의 포스팅을 draft 상태로 변경'.format(updated_count))  # django message framework 활용

    make_draft.short_description = '선택한 포스팅을 비공개 상태로 변경'

    fieldsets = (
        ('제목 및 내용', {
            'fields': (
                'email', 'image', 'title', 'tag', 'text',
            )
        }),
        ('작성일 및 배포일', {
            'fields': ('created_date', 'published_date',)
        })
    )