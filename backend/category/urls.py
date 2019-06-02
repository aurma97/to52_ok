from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', CategoryAPIView.as_view(), name="category-rud"),
    path('<pk>', CategoryRudView.as_view(), name="category-rud"),
]