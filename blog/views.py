from django.shortcuts import render, get_object_or_404
from .models import Post


def all_blogs(request):
    blog_count = Post.objects.count
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'blog_count': blog_count})


def detail(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
