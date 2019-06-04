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

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        #user.set_password(make_password(validated_data['password']))
        #user.save()
        return user

    class Meta:
        model = User
        fields = ('id','username', 'password', 'email')