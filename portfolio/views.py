from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.utils import timezone
from .models import Portfolio

def index(request):
    Portfolios = Portfolio.objects.filter(published_date__lte=timezone.now()).order_by(Coalesce('published_date','created_date').desc())
    return render(request, 'portfolio/index.html', {'Portfolios': Portfolios})


def plex(request):

    return render(request, 'portfolio/plex.html', {})

