from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'content',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


# 댓글 조회 시 게시글 출력 내역 변경 
class CommentSerializer(serializers.ModelSerializer):
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # 기존 article데이터 값을 override
    # 그런데 기존 필드를 override하면 Meta 클래스 read_only 필드 사용 불가능 
    article = ArticleTitleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # 유효성 검사에서 제외시키고 데이터 조회시에는 출력하는 필드
        # read_only_fields=('article',)