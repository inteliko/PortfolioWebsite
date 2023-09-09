from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    most_recent_post = Post.objects.order_by('-date_posted').first()
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'most_recent_post': most_recent_post, 'posts': posts})






from .models import Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.ip_address = get_client_ip(request)  # Add this line
            new_comment.save()

            # Redirect to the post detail page
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip




