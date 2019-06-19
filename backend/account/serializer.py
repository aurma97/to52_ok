from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
#from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(
        required = True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    first_name = serializers.CharField()
    
    last_name = serializers.CharField()

    is_staff = serializers.BooleanField()

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.first_name=validated_data['first_name']
        user.last_name=validated_data['last_name']
        user.is_staff = True
        return user

    class Meta:
        model = User
        fields = ('id','username', 'password', 'email', 'first_name', 'last_name', 'is_staff')

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'password', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')