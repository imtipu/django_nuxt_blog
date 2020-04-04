from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.api.v1.viewsets import *
router = DefaultRouter()
router.register(u'posts', BlogPostViewSet, basename='api_blog_posts')
router.register(u'categories', PostCategoryViewSet, basename='api_post_categories')
router.register(u'sub-categories', PostSubCategoryViewSet, basename='api_post_sub_categories')

urlpatterns = [
    path('', include(router.urls)),
]
