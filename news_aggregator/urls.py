from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView

urlpatterns = [
    # path('',views.post_list, name='post_list'),
      path('', PostListView.as_view(), name='post_list'),
      path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
      path('post/new/', PostCreateView.as_view(), name='post_create')
]

