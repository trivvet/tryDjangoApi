import collections
from json import loads, dumps
from django.contrib.auth import (
    get_user_model,
    hashers
    )
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
    )
User = get_user_model()

class AccountListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username', 
            'first_name',
            'last_name', 
            'email', 
            'is_staff', 
            'is_active', 
            'is_superuser', 
            'last_login'
        )

class AccountCreateSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
   
        }

    # def validate(self, data):
    #     data_dict = loads(dumps(data))
    #     print data_dict.password
    #     data_dict.password = hashers.make_password(data_dict.password)
    #     dict = collections.OrderedDict(data_dict)
    #     return data