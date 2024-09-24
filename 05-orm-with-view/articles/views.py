from django.shortcuts import render
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    # 게시글 작성 페이지 응답
    return render(request, 'articles/new.html')

def create(request):
    # 1. 사용자 요청으로부터 입력 데이터 추출
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 1번과 2번이 동일하다만, 1번은 너무 길기에 2번 사용
    # # 저장 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 저장 2
    article = Article(title = title, content = content)
    article.save()


    # 유효성 검사에서 탈락 쓰지마 
    # # 저장 3
    # Article.objects.create(title = title, content = content)

    # 2. 추출한 입력데이터를 활용해 DB에 저장 요청

    return render(request, 'articles/create.html')