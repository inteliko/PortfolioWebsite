from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    most_recent_post = Post.objects.order_by('-date_posted').first()
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'most_recent_post': most_recent_post, 'posts': posts})




def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
