from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# all supporting views
# Get all posts that have a published date
def post_list(request):
    #return render(request, 'blog/post_list.html', {})
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# Get the post that has the passed PK value
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


