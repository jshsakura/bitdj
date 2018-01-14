from django.db.models.functions import Coalesce
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Portfolio
from django.db.models import Q

def index(request):
    # POST 메소드의 검색어 조회
    search_text = request.POST.get('search_text', '')

    Portfolio_all_list = Portfolio.objects.filter(published_date__lte=timezone.now()).order_by(
        Coalesce('published_date', 'created_date').desc())
    # 검색어 존재여부 확인
    if search_text == '':
        # GET 방식으로 넘어온 검색어 조회
        search_text = request.GET.get('search_text', '')

    # 검색어 적용 조회
    if search_text != '':
        # __icontains 문자열 포함된 건만 조회
        Portfolios = Portfolio_all_list.filter(Q(title__icontains=search_text) | Q(tag__icontains=search_text))
    else:
        Portfolios = Portfolio_all_list



    return render(request, 'portfolio/index.html', {'Portfolios': Portfolios,'search_text':search_text})


def plex(request):

    return render(request, 'portfolio/plex.html', {})




# def create(request):
#     if request.method == "GET":
#         form = PortfolioForm()
#     elif request.method == "POST":
#         form = PortfolioForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             obj = form.save()
#             return redirect(obj)
#
#     ctx = {
#         'form': form,
#     }
#
#     return render(request, 'edit.html', ctx)