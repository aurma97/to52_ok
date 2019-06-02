from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', csrf_exempt(PostAPIView.as_view())),
    path('all', views.get_all_post),
    path('type', PostTypeAPIView.as_view(), name="post-create"),
    path('date/<pk>', PostRudView.as_view(), name="post-rud"),
    path('<pk>', views.get_post),
]
