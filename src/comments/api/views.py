from django.db.models import Q

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView
    ) 
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser
    )

from ..models import Comment
from .serializers import (
    CommentSerializer, 
    CommentDetailSerializer,
    CommentChildSerializer
    )

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = (
        'user__username',
        'content'
    )
    # ordering_fields = ('', 'content')
    # pagination_class = PostPagePagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(user__username__icontains=query)|
                Q(content__icontains=query)
                ).distinct()
        return queryset_list

# class CommentChildListAPIView(ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentChildSerializer
#     permission_classes = (IsAuthenticated, IsAdminUser)
#     lookup_field = 'parent'

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)