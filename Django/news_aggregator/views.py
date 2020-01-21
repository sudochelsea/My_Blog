from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from django.shortcuts import render

from .models import Post


# Create your views here.
# this is my home page
def post_list(request):

    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'news/post_list.html', context, )

class PostListView(ListView):
    model = Post
    template_name = 'news/post_list.html'
    context_name = 'posts'
    ordering = ['-created']


class PostDetailView(DetailView):
        model = Post
