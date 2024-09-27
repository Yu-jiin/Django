from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    # 중복가능한 문자열이 아니라, 고유한 값인 PK값을 기준으로 variable routing
    # 주소창에 사용자가 입력한 값에 따라서, 서로 다른 경로도 처리할 수 있어야 겠다.
    # 그런데, 정수 형태만 허용하겠다! <int: 변수명>
        # variable routing 방식으로 주소를 작성하게 되면
        # 그때 작성한 변수 todo_pk -> views.detail 함수를 호출 할때,
        # 키워드 인자의 변수명으로 사용된다.
            # detail(todo_pk = '사용자가 입력한 값')
    path('<int:todo_pk>/', views.detail, name='detail'),
    # 삭제? -> 뭘 삭제?
    # 삭제 대상의 고유값 -> PK,
    path('<int:todo_pk>/delete/', views.delete, name='delete'),
    # 원래 있었던 걸 수정 -> 뭘 수정?
    path('<int:todo_pk>/update/', views.update, name='update'),
    path('<int:todo_pk>/edit/', views.edit, name='edit'),
]