from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Post



# Create your views here.
#this is a function based view of post list on the home page
def post_list(request):

    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'news/post_list.html', context, )
    #this is the class based view of post list on the home page

class PostListView(ListView):
        model = Post
        template_name = 'news/post_list.html'
        # <app>/<model>_<viewt  ype>.html
        context_object_name = 'posts'
        ordering = ['-created']

#we are creating the class based view for detailview
class PostDetailView(DetailView):
        model = Post
        template_name = 'news/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
        model = Post
        fields = ['title', 'text']
        # template_name ='news/post_form.html'


        def form_valid(self, form):
            form.instance.author = self.request.user
            return  super().form_valid(form)