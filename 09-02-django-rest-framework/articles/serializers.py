from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')



class ArticleSerializer(serializers.ModelSerializer):
    # 역참조
    class CommentDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ('id', 'content')

    # 얘는 유효성 검사 대상이 아니기에 read_only 
    # 역참조 데이터를 override 
    comment_set = CommentDetailSerializer(many=True, read_only=True)
    # 여기서의 source = 필드를 채우는데 사용할 속성의 이름 . 표기법을 사용하여 속성 탐색 가능
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

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

# 결과
# {
#     "id": 1,
#     "article": {
#         "title": "Water behavior return interesting return understand."
#     },
#     "content": "Tonight free why name break. Fine receive become fear. Really break good executive something improve. Later month star now purpose loss with.",
#     "created_at": "1975-12-07T13:38:25Z",
#     "updated_at": "1991-01-16T06:45:10Z"
# }