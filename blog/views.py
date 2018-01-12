from django.db.models.functions import Coalesce
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Post
from .forms import UploadFileForm, PostForm
from django.http import HttpResponseRedirect

def post_list(request):
    user = request.user
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(Coalesce('published_date','created_date').desc())
    return render(request, 'blog/post_list.html', {'posts': posts,'user': user})


def contact(request):

    return render(request, 'blog/contact.html', {})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    user = request.user

    if request.method == 'POST': # 폼이 제출되었을 경우...
        form = PostForm(request.POST) # 폼은 POST 데이터에 바인드됨
        if form.is_valid(): # 모든 유효성 검증 규칙을 통과
            # form.cleaned_data에 있는 데이터를 처리
            title = form.cleaned_data['title']
            post_img = form.cleaned_data['post_img']
            tag = form.cleaned_data['tag']
            text = form.cleaned_data['text']
            sender = form.cleaned_data['sender']
            created_date = form.cleaned_data['created_date']
            published_date = form.cleaned_data['published_date']

            return HttpResponseRedirect('blog/post_list/') # Redirect after POST
    else:
        form = PostForm() # An unbound form

    return render_to_response('blog/post_new.html', {
        'form': form,'user':user,
    })

def post_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('blog/')
    else:
        form = UploadFileForm()
    return render(request, 'blog/upload.html', {'form': form})