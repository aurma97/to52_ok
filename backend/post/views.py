from django.db.models import Q
from rest_framework import generics, mixins
from .models import Post, PostType
from .permissions import IsOwnerOrReadOnly 
from .serializer import PostSerializer, PostDetailSerializer, PostTypeSerializer
from django.http import HttpResponse
from django.db import connection
import json

#See all objects and create someone
class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class= PostSerializer
    #authentication_class= (JSONWebTokenAuthentication,)
    #permission_classes= (IsAuthenticated,)

    def get_queryset(self): #for searching
        qs= Post.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostDetailAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class= PostSerializer
    #authentication_class= (JSONWebTokenAuthentication,)
    #permission_classes= (IsAuthenticated,)

    def get_queryset(self): #for searching
        qs= Post.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class PostTypeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class= PostTypeSerializer

    def get_queryset(self): #for searching
        qs= PostType.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs= qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

# See specific thing
class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class= PostDetailSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    
    #queryset = Post.objects.all()

    def get_queryset(self):

        post = Post.objects.all()

        return post
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)
