from django.shortcuts import render
from django.views import generic
from blog.models import *
# Create your views here.


def blog_home(request):
    data = {
        'title': 'Home'
    }
    return render(request, 'blog/home.html', data)


class CategoryPosts(generic.ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/categories/posts.html'

    def get_queryset(self):
        return BlogPost.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = PostCategory.objects.get(slug=self.kwargs['slug'])
        return context


class SubCategoryPosts(generic.ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/categories/posts.html'

    def get_queryset(self):
        return BlogPost.objects.filter(sub_category__slug=self.kwargs['sub_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = PostSubCategory.objects.get(slug=self.kwargs['sub_slug'])
        return context


class PostDetail(generic.DetailView):
    model = BlogPost
    context_object_name = 'post'
    template_name = 'blog/posts/detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class TagsPost(generic.ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'blog/tags/posts.html'

    def get_queryset(self):
        return BlogPost.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['tag'] = PostTag.objects.get(slug=self.kwargs['slug'])
        return context