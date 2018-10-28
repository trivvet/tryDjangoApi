import collections
from json import loads, dumps
from django.contrib.auth import (
    get_user_model,
    hashers
    )
from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError,
    EmailField,
    CharField
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
    email2 = EmailField(label="Confirm Email")
    password_repeat = CharField(label="Confirm Password")
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            'password_repeat'
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
    
    def validate(self, data):
        email = data['email']
        email2 = data['email2']
        password = data['password']
        password_repeat = data['password_repeat']
        users_email = User.objects.filter(email=email)
        if users_email.exists():
            raise ValidationError({'email': "This email is already used!"})
        if email != email2:
            raise ValidationError({
                'email': "Emails in both fields must be the save"
            })
        if password != password_repeat:
            raise ValidationError({
                'password': "Passwords in both fields must be the same"
            })
        return data

    def create(self, validated_data):
        new_user = {}
        new_user['username'] = validated_data['username']
        new_user['first_name'] = validated_data['first_name']
        new_user['last_name'] = validated_data['last_name']
        new_user['email'] = validated_data['email']
        user = User(**new_user)
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class AccountLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(label="Username")
    email = EmailField(label="Email")
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'token'
        )
        write_only_fields = ('password')
    
    def validate(self, data):
        return data