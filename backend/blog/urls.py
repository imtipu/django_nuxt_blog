from django.urls import path
from blog import views
urlpatterns = [
    path('<str:slug>/', views.CategoryPosts.as_view(), name='category_post'),
    path('<str:slug>/<str:sub_slug>', views.SubCategoryPosts.as_view(), name='sub_category_post'),
    path('posts/<str:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('tags/<str:slug>/', views.TagsPost.as_view(), name='tags_post'),
]
