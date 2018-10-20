from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )

from ..models import Comment


class CommentSerializer(ModelSerializer):
    # children_list_url = HyperlinkedIdentityField(
    #     view_name="comments-api:comments_child_list",
    #     lookup_field='id')
    reply_count = SerializerMethodField()
    # detail_url = HyperlinkedIdentityField(
    #     view_name="comments-api:comment_detail")

    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content_type',
            'content',
            'parent',
            # 'children_list_url',
            # 'detail_url',
            'reply_count'
        )

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        else:
            return 0

class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'content',
            'timestamp',
            'parent'
        )

class CommentDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'content_type',
            'content',
            'replies',
            'reply_count'
        )

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), 
                many=True).data

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        else:
            return 0
