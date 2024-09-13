from django.shortcuts import render

# Create your views here.

# request 개필수
def index(request):
    # 메인페이지를 응답
    return render(request, 'articles/index.html')