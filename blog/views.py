import json
from django.views.generic import ListView, DetailView
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm
from  blog.models import Post
# Create your views here.
class ListPostView(ListView):
   queryset = Post.objects.all().order_by('-date')
   template_name = 'blog/blog.html'
   context_object_name = 'Posts'
   paginate_by = 1
class PosteDetail(DetailView):
    model = Post
    template_name='blog/post.html'
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, "blog/post.html", {"post": post,"form": comment_form})
def postComment(request, pk):
   post = get_object_or_404(Post, pk=pk)
   comment_form = CommentForm()
   if(request.method == "POST"):
      # print(request.POST["body"])
      body = request.POST['body']
      form = CommentForm(request.POST,body=body,author=request.user, post=post)#request.POST để check form xem form có hợp lệ không
      if form.is_valid():
         print("savingggggggggg")
         form.save()
         return HttpResponseRedirect("/blog/" + str(post.pk))
      else:
         print("hichic")
   return render(request, "blog/post.html", {"post": post,"form": comment_form})


