from django.http import HttpResponse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .serializer import UserSerializer, UserDetailSerializer
import json

@api_view(['GET'])
def current_user(request):
    serializer = UserDetailSerializer(request.user)
    return Response(serializer.data)

@csrf_exempt
def login_user (request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("success")
        else:
            return HttpResponse("error")
        return HttpResponse(username)
        
@csrf_exempt
def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponse('Logout successful')

class CsrfExempt(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class AccountAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    authentication_classes = (CsrfExempt, BasicAuthentication)
    serializer_class= UserSerializer

class AccountRudView(generics.RetrieveUpdateDestroyAPIView):
    #lookup_field = 'pk'
    serializer_class = UserSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)
    queryset = User.objects.all()

    # def get_object(self):
    #     username = self.kwargs["username"]
    #     obj = get_object_or_404(User, username = username)
    #     return obj
    
    # def put (self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)