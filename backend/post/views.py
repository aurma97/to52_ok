from django.db.models import Q
from rest_framework import generics, mixins
from .models import Post, PostType
from .permissions import IsOwnerOrReadOnly 
from .serializer import PostSerializer, PostTypeSerializer
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

    def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

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
    serializer_class= PostSerializer
    permissions_classes = [IsOwnerOrReadOnly]
    
    #queryset = Post.objects.all()

    def get_queryset(self):

        post = Post.objects.all()
    

        return post
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)

def get_post(request, pk):


    def dictfetchall(cursor):
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()]


    if request.method == 'GET':
        
        #t = Post.objects.get(pk=pk)
        #post = Post.objects.raw('SELECT p.id, p.title as "title_post" FROM post_post p')
        cursor = connection.cursor()
        post = cursor.execute('''SELECT p.id, p.title, t.title as type, p.price, p.content, p.num_street, p.street, p.city, p.postalcode, p.country, p.image_one, p.image_two, p.image_three, c.title as "Category_title", u.username FROM post_post p inner join category_category c ON p.category_id = c.id INNER JOIN auth_user u ON u.id = p.author_id INNER JOIN post_posttype t ON p.an_type_id = t.id  WHERE p.id = ''' + pk)
        post = dictfetchall(post)

        post = json.dumps(post)
        
        return HttpResponse(post)
    return HttpResponse("Erreur")


def get_all_post(request):

    def dictfetchall(cursor):
        desc = cursor.description
        return [dict(zip([col[0] for col in desc], row))
                for row in cursor.fetchall()]

    if request.method == 'GET':
        
        #t = Post.objects.get(pk=pk)
        #post = Post.objects.raw('SELECT p.id, p.title as "title_post" FROM post_post p')
        cursor = connection.cursor()
        posts = cursor.execute('''SELECT p.id, p.title, t.title as type, p.price, p.content, p.num_street, p.street, p.city, p.postalcode, p.country, p.image_one, p.image_two, p.image_three, c.title as "Category_title", u.username FROM post_post p inner join category_category c ON p.category_id = c.id INNER JOIN auth_user u ON u.id = p.author_id INNER JOIN post_posttype t ON p.an_type_id = t.id''')
        posts = dictfetchall(posts)

        posts = json.dumps(posts)
        
        return HttpResponse(posts)

    return HttpResponse("Erreur")