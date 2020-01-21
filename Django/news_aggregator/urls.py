from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # path('',views.post_list, name='post_list'),
     path('', PostListView.as_view(),name='post_list'),
     path('post/<int:pk>/', PostDetailView.as_view(),name='post_detail'),
]

