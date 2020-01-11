from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from blog.models import Post, Tag


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags': tags})


# class TagDetail(View):
#     def get(self, request, slug):
#         tag = get_object_or_404(Tag, slug_iexact=slug)
#         return render(request, 'blog/tag_detail.html', context={'tag': tag})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': post})


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag': tag})

