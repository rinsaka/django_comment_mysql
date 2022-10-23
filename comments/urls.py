from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.CommentIndexView.as_view(), name='index'),
    path('<int:pk>/', views.ShowCommentView.as_view(), name='show'),
    path('create/', views.CreateCommentView.as_view(), name='create'),
]