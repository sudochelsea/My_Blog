from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    # STATUS_CHOICES = (('draft', 'Draft'),('published','Publshed'),)
    title = models.CharField(max_length=50)
    # slug = models.SlugField(max_length=250,unique_for_dates='publish')
    # author = models.CharField(max_lenght=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    # status = models.CharField(max_length=10,choices=STATUS_CHOICES,default = 'draft')

    def __str__(self):
        return self.title