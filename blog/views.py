from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def post_list(request):
    most_recent_post = Post.objects.order_by('-date_posted').first()
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'most_recent_post': most_recent_post, 'posts': posts})




from .models import Post, Comment
from .forms import CommentForm


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            # Redirect to the post detail page
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})