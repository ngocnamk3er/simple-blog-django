from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render
from .models import Post
# Create your views here.
class ListPostView(ListView):
   queryset = Post.objects.all().order_by('-date')
   template_name = 'blog/blog.html'
   context_object_name = 'Posts'
   paginate_by = 1
class PosteDetail(DetailView):
    model = Post
    template_name='blog/post.html'

