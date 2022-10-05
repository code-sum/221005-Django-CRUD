from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    # 게시글을 가져와서..
    # (보통 게시판은 최신글이 맨위니까 .order_by('-pk') 활용)
    articles = Article.objects.order_by('-pk')
    # template 에 뿌려준다
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: # request.method == 'GET':
        # 일반적인 사이트들은 유효하지 않을 때
        # 이슈가 발생한 페이지를 보여주고 정정하라고 하는데,
        # ModelForm 활용해서 new.html 로 넘겨주라고 else 문 작성하면
        # 우리가 원했던 기능이 구현됨
        article_form = ArticleForm()
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/new.html', context=context)

def detail(request, pk):
    # 특정 글을 가져온다.
    article = Article.objects.get(pk=pk)
    # template 에 객체 전달
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # POST : input 가져와서 검증하고 DB 에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장후 상세보기 페이지로
            article_form.save()
            return redirect('articles:detail', article.pk)
        # 유효성 검사 통과 못하면 => 오류메세지
    else: 
        # GET 처리 : Form 을 제공
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form
    }
    return render(request, 'articles/update.html', context)