
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]

# url app으로 나누기
    # 1. include 추가 
    # 2. path('articles/', include('articles.urls')), 추가
    # 3. articles 밑에 urls.py 만들기 
    # 4. 기존 url에서 긁어와서 필요없는거 지우고 바꾸기 
        # from django.urls import path
        # from . import views

        # app_name = 'articles'
        # urlpatterns = [
        #     path('', views.index, name='index'),
        # ]

    # 후에 views에 index 함수 작성 
    # def index(request):
    #     return render(request, 'articles/index.html')

    # 5. articles 밑에 templates/articles/index.html 생성