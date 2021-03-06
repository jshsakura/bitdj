from django.contrib.auth.decorators import login_required
from django.contrib.redirects.models import Redirect
from django.db.models.functions import Coalesce
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.views.decorators.http import require_POST

from .models import Post, Comment
from .forms import UploadFileForm, PostForm, CommentForm ,ContactForm
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.db.models import Q
from account.slacker import slack_notify


def post_list(request):
    #POST 메소드의 검색어 조회
    search_text = request.POST.get('search_text', '')
    #검색어 존재여부 확인
    if search_text == '':
        # GET 방식으로 넘어온 검색어 조회
        search_text = request.GET.get('search_text', '')

    #posts_all = Post.objects.filter(published_date__lte=timezone.now() & (Q(title=search_text) | Q(tag=search_text))).order_by(Coalesce('published_date','created_date').desc())

    posts_all_list = Post.objects.filter(published_date__lte=timezone.now()).order_by(Coalesce('published_date', 'created_date').desc())

    #검색어 적용 조회
    if search_text != '':
        # __icontains 문자열 포함된 건만 조회
        posts_all = posts_all_list.filter(Q(title__icontains=search_text) | Q(tag__icontains=search_text))
    else:
        posts_all = posts_all_list

    # 조회수 탑4
    post_top4 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-hit')[:4]
    # 페이징 처리를 위한 페이지네이터 pip 으로 설치
    paginator = Paginator(posts_all, 5)  # Show 20 contacts per page

    try:
        page = request.GET.get('page','1')
    except:
        page = 1

    try:
        post_paging = paginator.page(page)
    except(EmptyPage, InvalidPage):
        post_paging = paginator.page(1)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_paging = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_paging = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': post_paging, 'top4':post_top4, 'search_text':search_text})




def post_detail(request, pk):
    search_text = request.GET.get('search_text', '')
    #조회수 탑4
    post_top4 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-hit')[:4]

    post = get_object_or_404(Post, pk=pk)
    post.hit = (post.hit + 1)
    post.save()

    return render(request, 'blog/post_detail.html', {'post': post, 'top4':post_top4, 'search_text':search_text})

#코멘트 작성 뷰
@require_POST
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            attachments = [{
                "color": "#da521e",
                "author_name": comment.name,
                "author_link": "http://jshsakura.iptime.org/post/"+pk,
                "author_icon": 'http://jshsakura.iptime.org/media/profile_image/2018/01/15/download.jpeg',
                "title": post.title,
                "title_link": "http://jshsakura.iptime.org/post/"+pk,
                "fallback": "신규 코멘트 알림",
                "text": "{}".format(comment.text)
            }]
            slack_notify(text='신규 COMMENT 알림' ,channel='#django_blog', username='Django Bot', attachments=attachments)
            return redirect('post_detail', pk=post.pk)
    else:
        #form = CommentForm()
        return redirect('post_detail', pk=post.pk)

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

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
            form.save()
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


def contact(request):
    search_text = request.GET.get('search_text', '')
    # 조회수 탑4
    post_top4 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-hit')[:4]
    if request.method == 'POST': # 폼이 제출되었을 경우...
        form = ContactForm(request.POST) # 폼은 POST 데이터에 바인드됨
        if form.is_valid(): # 모든 유효성 검증 규칙을 통과
            # form.cleaned_data에 있는 데이터를 처리
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            form.save()

            attachments = [{
                "color": "#da521e",
                "author_name": name,
                "author_link": "http://jshsakura.iptime.org/admin/blog/contact/"+form.auto_id+"/change/",
                "author_icon": 'http://jshsakura.iptime.org/media/profile_image/2018/01/15/download.jpeg',
                "title": email,
                "title_link": "http://jshsakura.iptime.org/admin/blog/contact/"+form.auto_id+"/change/",
                "fallback": "신규 CONTACT US 알림",
                "text": "{}".format(text)
            }]
            slack_notify(text='신규 CONTACT US 알림', channel='#django_blog', username='Django Bot', attachments=attachments)
            return render(request, 'blog/contact_ok.html', {'top4': post_top4})
    else:
            return render(request, 'blog/contact.html', {'top4': post_top4})

def contact_ok(request):
    # 조회수 탑4
    post_top4 = Post.objects.filter(published_date__lte=timezone.now()).order_by('-hit')[:4]
    return render(request, 'blog/contact_ok.html', {'top4': post_top4})

#### test writer page

#@login_required
def write_form(request):
	page_title = 'write page'
	tem = loader.get_template('write.html')
	cont= Context({
			'page_title':page_title
		}
	)
	return HttpResponse (tem.render(cont))
	
