from __future__ import unicode_literals
from django import forms
from django.conf import settings
from .widgets import SimpleMDEWidget
from .models import Portfolio

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = Portfolio
#         fields = ('title', 'file')
#
#     def __init__(self, *args, **kwargs):
#         super(Portfolio, self).__init__(*args, **kwargs)
#         self.fields['file'].required = False
#
#
# class PostForm(forms.Form):
#     author = forms.EmailField()
#     title = forms.CharField(max_length=100)
#     post_img = forms.CharField(max_length=100)
#
#     text = forms.CharField()
#     tag = forms.CharField(max_length=100)
#
#     created_date = forms.DateField(required=False)
#     published_date = forms.DateField(required=False)