from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('all', AccountAPIView.as_view()),
    path('user/', views.current_user),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('register', AccountAPIView.as_view()),
    path('update/<pk>', AccountRudView.as_view())
]