from django.contrib import admin
from django.forms import forms, models
from django.utils.safestring import mark_safe
from django.utils import timezone
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.settings import summernote_config, get_attachment_model

from .models import Post, Contact , Comment
#admin.site.register(Post.ModelAdmin);

admin.site.register(Comment)

__widget__ = SummernoteWidget if summernote_config['iframe'] \
    else SummernoteInplaceWidget

class PostAdmin(SummernoteModelAdmin):
    list_per_page = 15
    list_display = ['id', 'title','tag', 'text_size', 'hit', 'created_date','published_date', ]
    list_display_links = ['id', 'title']
    ordering = ('-published_date',)

    actions = ['make_published', 'make_draft']

    summer_note_fields = ('text',)

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

admin.site.register(Post, PostAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'name', 'email', 'text', 'created_date','published_date', ]
    list_display_links = ['id', 'name', 'email']
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



    #작성폼 수정
    fieldsets = (
        ('제목 및 내용', {
            'fields': (
                'name', 'email', 'image', 'text',
            )
        }),
        ('작성일 및 배포일', {
            'fields': ('created_date', 'published_date',)
        })
    )