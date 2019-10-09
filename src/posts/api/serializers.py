from rest_framework import serializers

from posts.models import Post

#HyperlinkedIdentityField is used to get details in url
class PostSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name = 'posts-api-list:detail',
            lookup_field = 'slug'
        )
    delete_url = serializers.HyperlinkedIdentityField(
        view_name = 'posts-api-list:delete',
        lookup_field = 'slug'
    )
    class Meta:
        model = Post
        fields = [
            'delete_url',
            'url',
            'user',
            'id',
            'title',
            'content',
            'publish'
        ]

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'content',
            'publish'
        ]