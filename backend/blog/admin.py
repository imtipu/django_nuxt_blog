from django.contrib import admin
from blog.models import *
# Register your models here.


class PostTagInline(admin.TabularInline):
    model = PostTag
    extra = 2


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'created']
    readonly_fields = ['post_thumbnail', ]
    filter_horizontal = ['tags', ]


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created']


@admin.register(PostSubCategory)
class PostSubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent', 'created']


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'slug', 'created']


# @admin.register(BlogPost)
# class BlogPostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'created']
