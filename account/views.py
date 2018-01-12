from django.shortcuts import render
from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView


class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('common:register_done') # 네임스페이스 정확하게

class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'