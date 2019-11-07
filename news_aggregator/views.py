from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):

    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'news/post_list.html', context, )