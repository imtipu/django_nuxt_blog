from rest_framework import serializers
from blog.models import *

User = get_user_model()


class AuthorReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'date_joined',)
        read_only_fields = ('first_name', 'last_name', 'email', 'username', 'date_joined',)


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = '__all__'


class PostSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostSubCategory
        fields = '__all__'


class PostCategorySerializer(serializers.ModelSerializer):
    sub_categories = PostSubCategorySerializer(source='subcategory_parent', read_only=True, many=True,)

    class Meta:
        model = PostCategory
        depth = 2
        fields = [
            'id',
            'name',
            'slug',
            'sub_categories',
        ]


class BlogPostSerializer(serializers.ModelSerializer):
    tags = PostTagSerializer(read_only=True, many=True)
    author = AuthorReadSerializer(read_only=True, many=False)
    category = PostCategorySerializer(read_only=True, many=False)
    sub_category = PostSubCategorySerializer(read_only=True, many=False)

    class Meta:
        model = BlogPost
        fields = '__all__'



