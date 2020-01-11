from django.shortcuts import render, redirect
from django.views.generic import View
from blog.models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'
    # def get(self, request):
    #     form = PostForm()
    #     return render(request, 'blog/post_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'blog/post_create.html', context={'form': bound_form})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'
    # def get(self, request):
    #     form = TagForm()
    #     return render(request, 'blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'blog/tag_create.html', context={'form': bound_form})

