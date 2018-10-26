from django.contrib.auth import (
    get_user_model
    )
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
    ) 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (
    AccountListSerializer,
    AccountCreateSerializer
    )
User = get_user_model()

class AccountListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountListSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class AccountCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AccountCreateSerializer