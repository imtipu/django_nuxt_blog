from django import template
from blog.models import *

register = template.Library()


@register.simple_tag(name='post_categories')
def post_categories():
    return PostCategory.objects.all().iterator()


@register.simple_tag(name='home_featured_post')
def home_featured_post():
    return BlogPost.objects.all().prefetch_related('category', 'author', 'sub_category').last()


@register.simple_tag(name='recent_posts')
def recent_posts():
    return BlogPost.objects.all().prefetch_related('category', 'author', 'sub_category').order_by('-created')[:5]


@register.simple_tag(name='test_str')
def test_str():
    data = {
       'test_str': 'test_str'
    }
    return data