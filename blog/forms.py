from django import forms
from django.forms import ModelForm
from django.utils import timezone

from .models import UploadFileModel
from .models import Post, Comment ,Contact

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.fields['file'].required = False


class PostForm(forms.Form):
    email = forms.EmailField()
    image = forms.ImageField()
    post_img = forms.CharField(max_length=100)
    tag = forms.CharField(max_length=100)
    text = forms.CharField()

    created_date = forms.DateField(required=False)
    published_date = forms.DateField(required=False)


    #어드민 글자 관련 제약조건 테스트
    # def clean_content(forms.ModelForm):  # clean_{field_name}
    #     Post.text = self.cleaned_data['text']
    #
    #     words = ['운지', '노무현', '시발']
    #     error_message ='[{0}] {1}'.format(', '.join(words), '과 같은 단어는 작성할 수 없습니다....')
    #     if any(word in text for word in words):
    #         raise forms.ValidationError(error_message)
    #     return text

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'text',)


class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=255)
    # image = forms.ImageField()
    # text = forms.CharField(max_length=100)
    # created_date = forms.DateField(required=False)
    # published_date = forms.DateField(required=False)
    class Meta:
        model = Contact
        fields = ('name', 'email', 'text',)
