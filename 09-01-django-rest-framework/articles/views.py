from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializer import ArticleListSerializer, ArticleSerializer

# api_view = 기본값은 GET, 필수로 작성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # 다중데이터라 many=True, 단일은 안써도됨 
        serializer = ArticleListSerializer(articles, many=True)
        # .data = 실제 데이터 추출 
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = request.data로 .. 
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 저장 성공 후 201 반환
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        # 유효성 검사 실패 후 400 응답 상태코드 반환 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 직렬화
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 삭제 
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # 수정 
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    