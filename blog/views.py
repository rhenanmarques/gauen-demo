from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.urls import reverse
from blog.models import Category, Post
from utils.gauenPublic.pagination import make_pagination
from django.db.models import Q
from utils.gauenPublic.djangoViews import CheckCookies


def blog(request):
    posts = Post.objects.filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, posts, 9)
    context= {
        'posts': page_obj, 
        'pagination_range': pagination_range}

    CheckCookies(request, context)

    return render(request, 'blog/pages/blog.html', context)


def category(request, slug):
    posts = get_list_or_404(Post.objects.filter(is_published=True, category__slug=slug).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, posts, 9)

    context={
        'title': f'{posts[0].category.name}',
        'posts': page_obj, 
        'pagination_range': pagination_range}

    CheckCookies(request, context)

    return render(request, 'blog/pages/category.html', context)


def postRead(request, slug):
    categories = Category.objects.all()
    post = get_object_or_404(Post, slug=slug, is_published=True)
    otherPosts = Post.objects.filter(is_published=True).order_by('-id')[:3]
    context = {
        'content': post,
        'categories': categories,
        'more': otherPosts,
    }

    CheckCookies(request, context)
    return render(request, 'blog/pages/postRead.html', context)


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    posts = Post.objects.filter(
        Q(
            Q(title__icontains= search_term) |
            Q(description__icontains= search_term)
        ),
        is_published=True
    ).order_by('-id')

    context = {
        'page_title': f'Pesquisa por "{search_term}"', 
        'search_term': search_term, 
        'posts': posts
    }

    return render(request, 'blog/pages/search.html', context)
