from django.shortcuts import render
# 모델 클래스 가져와
from .models import Article
# Create your views here.
def index(request):
    # 전체 조회
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)