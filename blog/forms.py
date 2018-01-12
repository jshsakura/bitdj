from django import forms

from .models import UploadFileModel
from .models import Post

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.fields['file'].required = False


class PostForm(forms.Form):
    sender = forms.EmailField()
    title = forms.CharField(max_length=100)
    post_img = forms.CharField(max_length=100)
    tag = forms.CharField(max_length=100)
    text = forms.CharField()

    created_date = forms.DateField(required=False)
    published_date = forms.DateField(required=False)