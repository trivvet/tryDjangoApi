from rest_framework.serializers import ModelSerializer

from ..models import Post

class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','user', 'title', 'content', 'image', 'draft', 'publish')

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