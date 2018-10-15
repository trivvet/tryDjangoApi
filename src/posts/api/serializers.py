from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedModelSerializer,
    HyperlinkedIdentityField
    )

from ..models import Post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:post_detail',
        lookup_field='pk')

    edit_url = HyperlinkedIdentityField(
        view_name="posts-api:post_update",
        lookup_field='pk')

    class Meta:
        model = Post
        fields = (
            'url', 
            'edit_url',
            'user', 
            'title', 
            'content', 
            'image', 
            'slug', 
            'publish')

    # def create(self)

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'publish')

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'publish')


    # title = serializers.CharField(max_length=200)
    # content = serializers.CharField()
    # image = serializers.ImageField()
    # draft = serializers.BooleanField()
    # publish = serializers.DateField()