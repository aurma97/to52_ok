"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from django.conf import settings
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api.views import index_view, MessageViewSet 

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
    path('api/manage/account/', include('backend.account.urls')),
    path('api/manage/category/', include('backend.category.urls')),
    path('api/manage/post/', include('backend.post.urls')),

    path('api/auth/obtain_token/', obtain_jwt_token),
    path('api/auth/refresh_token/', refresh_jwt_token),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)