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