from django.urls import path
from . import views

app_name="boards"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'), 
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),   
    path('<int:board_pk>/comment/', views.comment, name='comment'),
    path('<int:board_pk>/comment/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
    # path(
    #     '<int:article_pk>/comments/<int:comment_pk>/delete/',
    #     views.comments_delete,
    #     name='comments_delete',
    # ),
    path('<int:board_pk>/likes/', views.likes, name='likes'),
    path('comment/<int:comment_pk>/', views.create_reply, name='create_reply'),
]
