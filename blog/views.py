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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})


