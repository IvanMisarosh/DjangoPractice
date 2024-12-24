from django.shortcuts import render, get_object_or_404

from django.http import Http404

from .models import Post

# Create your views here.

def starting_page(request):
    # Django builds query so that slicing is done in the database
    latest_posts = Post.objects.all().order_by('-date')[:3]

    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })

def posts(request):
    return render(request, 'blog/all_posts.html', {
        'all_posts': Post.objects.all()
    })

def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
        
    return render(request, 'blog/post_detail.html', {
        'post': identified_post,
        'post_tags': identified_post.tags.all()
    })
