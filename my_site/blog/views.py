from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView

from .models import Post
from .forms import CommentForm

# Create your views here.
class StartingPageView(View):
    def get(self, request):
        # Django builds query so that slicing is done in the database
        latest_posts = Post.objects.all().order_by('-date')[:3]

        return render(request, 'blog/index.html', {
            'posts': latest_posts
        })

class PostsView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'
    context_object_name = 'all_posts'

class PostDetailView(View):
    def is_stored_post(self, request, post_slug):
        stored_posts = request.session.get('read_later', [])
        return post_slug in stored_posts

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
            'post': post  
        }
        context['comment_form'] = CommentForm()
        context['post_tags'] = post.tags.all()        
        context['is_read_later'] = self.is_stored_post(request, post.slug)
        context['comments'] = post.comments.all().order_by('-id')

        return render(request, 'blog/post_detail.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))
        
        
        context = {
            'post': post  
        }
        context['comment_form'] = comment_form
        context['post_tags'] = post.tags.all()        
        context['is_read_later'] = self.is_stored_post(request, post.slug)
        context['comments'] = post.comments.all().order_by('-id')
        return render(request, 'blog/post_detail.html', context)

class ReadLaterView(View):
    def get(self, request):
        read_later_posts_slugs = request.session.get('read_later') or []
 
        read_later_posts = Post.objects.filter(slug__in=read_later_posts_slugs)
        return render(request, 'blog/read_later.html', {
            'read_later_posts': read_later_posts
        })
    
    def post(self, request):
        post_slug = request.POST['post_slug']

        read_later_list = request.session.get("read_later")

        if not read_later_list:
            read_later_list = []

        if post_slug in read_later_list:
            read_later_list.remove(post_slug)
        else:
            read_later_list.append(post_slug)
            
        request.session['read_later'] = read_later_list
        return HttpResponseRedirect(reverse('post-detail-page', args=[post_slug]))

        

        
        
