# your_app/context_processors.py
from .models import Post

def recent_posts(request):
    most_recent_posts = Post.objects.order_by('-date_posted')[:3]  # Adjust the number of posts as needed
    return {'recent_posts': most_recent_posts}
