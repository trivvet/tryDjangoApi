from rest_framework.serializers import ModelSerializer

from ..models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content_type',
            'content',
            'object_id',
            'parent'
        )