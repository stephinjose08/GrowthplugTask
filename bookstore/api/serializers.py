
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from ..models import ebook,genreCategory


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

    
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        

        return token


class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password','id','is_active']
        extra_kwargs={
            'password':{'write_only':True},
            'is_active':{'default':True}
        }
    def create(self, validated_data):
        pwd = validated_data.pop("password")
        instance=self.Meta.model(**validated_data)
        instance.set_password(pwd)
        instance.save()
        return instance

    
class bookSerializer(serializers.ModelSerializer):
    users=RegisterSerializer(many=True,read_only=True)
    class Meta:
        model=ebook
        fields='__all__'

class genCategorySerializer(serializers.ModelSerializer):
    ebooks=bookSerializer(many=True,read_only=True)
    class Meta:
        model=genreCategory
        fields='__all__'