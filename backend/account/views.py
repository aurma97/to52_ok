from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import json

def current_user(request):
    current_user = request.user
    return HttpResponse(current_user.username)

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