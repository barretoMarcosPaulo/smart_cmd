from django.conf import settings
from django.urls import path
from django.contrib import admin
from django.urls import include
from rest_framework import permissions, routers

router = routers.SimpleRouter()


urlpatterns = [

    path("admin/", admin.site.urls),
    path('', include('core.urls')),
]
