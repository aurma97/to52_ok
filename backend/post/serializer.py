from rest_framework import serializers
from .models import Post, PostType

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('__all__')
        read_only_fields = ['id']

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields =('__all__')
        depth = 1
        read_only_fields = ['id']

    # def validate_title(self, value):
    #     qs = Post.objects.filter(title__iexact=value)
    #     if self.instance:
    #         qs = qs.exclude(pk=self.instance.pk)
    #     if qs.exists():
    #         raise serializers.ValidationError("The title must be unique")
    #     return value

class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = [
            'id',
            'title',
        ]
        read_only_fields = ['id']