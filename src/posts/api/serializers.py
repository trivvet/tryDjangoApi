from rest_framework.serializers import ModelSerializer

from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'draft', 'publish')

    # def create(self)

    # title = serializers.CharField(max_length=200)
    # content = serializers.CharField()
    # image = serializers.ImageField()
    # draft = serializers.BooleanField()
    # publish = serializers.DateField()