from django.db.models import Q
from rest_framework import generics, mixins
from .models import Category
from .serializer import CategorySerializer

class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class= CategorySerializer

    def get_queryset(self): #for searching
        qs= Category.objects.all()
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

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)



class CategoryRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class= CategorySerializer
    #queryset = Category.objects.all()

    def get_queryset(self):
        return Category.objects.all()
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Post.objects.get(pk=pk)