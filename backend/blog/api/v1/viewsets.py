from rest_framework import views, viewsets

from blog.api.v1.serializers import *
from blog.models import *


class BlogPostViewSet(viewsets.ModelViewSet):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class PostCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostCategorySerializer
    queryset = PostCategory.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'


class PostSubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = PostSubCategorySerializer
    queryset = PostSubCategory.objects.all()
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'
