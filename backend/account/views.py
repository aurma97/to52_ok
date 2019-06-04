from django.http import HttpResponse
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .permissions import AllowAny 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .serializer import UserSerializer
import json

@api_view(['GET'])
def current_user(request):
    # current_user = request.user
    # user = [current_user.username, current_user.id]
    # return HttpResponse(user)
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

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
        
def logout_user(request):
    if request.method == 'POST':
        logout(request)
    return HttpResponse('Logout successful')

class AccountAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class= UserSerializer
   

def register_user(request):
    form = request.POST

    if form.is_valid():
        form.save()
    return HttpResponse('Logout successful')