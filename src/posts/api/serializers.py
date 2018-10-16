from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from ..models import Post

class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:post_detail',
        lookup_field='pk')
    edit_url = HyperlinkedIdentityField(
        view_name="posts-api:post_update",
        lookup_field='pk')
    user = SerializerMethodField()

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
            'publish'
        )

    def get_user(self, obj):
        return obj.user.username

    # def create(self)

class PostDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            'title', 
            'content', 
            'user', 
            'image', 
            'publish',
            'html'
        )

    def get_user(self, obj):
        return obj.user.username

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        else:
            return None

    def get_html(self, obj):
        return obj.get_markdown()

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'image', 'publish')


    # title = serializers.CharField(max_length=200)
    # content = serializers.CharField()
    # image = serializers.ImageField()
    # draft = serializers.BooleanField()
    # publish = serializers.DateField()