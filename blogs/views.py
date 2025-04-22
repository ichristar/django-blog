from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, category
from django.db.models import Q

from dashboards.forms import BlogPostForm

# Create your views here.

def posts_by_category(request, category_id):
    
    posts = Blog.objects.filter(status='published', category=category_id)
    #categorys = category.objects.get(pk=category_id)
    
    #categorys = get_object_or_404(category, pk=category_id)
    
    try:
        categorys = category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    context = {
        'posts': posts,
        'category': categorys,

    }
    
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    
    single_blog = get_object_or_404(Blog, slug=slug)
    context = {
        'single_blog': single_blog,
        
    }
    
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
    
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    
    return render(request, 'search.html', context)

def add_post(request):
    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_post.html', context)