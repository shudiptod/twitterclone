from django.urls import path
from .views import (
    PostCreateView,
    PostDetailView,
    UserPostListView,
    FollowsListView,
    FollowersListView,
    postpreference,
    PostUpdateView,
    PostDeleteView
    )
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/',PostDetailView.as_view(),name="post_detail"),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('user/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('user/<int:pk>/delete',PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>/follows', FollowsListView.as_view(), name='user-follows'),
    path('user/<str:username>/followers', FollowersListView.as_view(), name='user-followers'),
    path('post/<int:postid>/preference/<int:userpreference>', postpreference, name='postpreference'),

    
]
