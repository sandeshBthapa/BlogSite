from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreatView,
                    PostUpdateView,
                    PostDeletView,
                    add_comment_to_post,
                    UserPostListView,
                    about, )

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about', about, name='about'),
    path('create', PostCreatView.as_view(), name='create'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/delete/', PostDeletView.as_view(), name='blog-delete'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='blog-update'),
]
