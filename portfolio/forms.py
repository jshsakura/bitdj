from __future__ import unicode_literals
from django import forms
from django.conf import settings
from .widgets import SimpleMDEWidget
from .models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ('image', 'title', )