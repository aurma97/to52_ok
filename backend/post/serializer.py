from rest_framework import serializers
from .models import Post, PostType

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'an_type',
            'price', 
            'content',
            'num_street',
            'street',
            'city',
            'postalcode', 
            'country',
            'image_one',
            'image_two',
            'image_three',
            'category',
            'author',
            'created_at',
            'updated_at',
        ]
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