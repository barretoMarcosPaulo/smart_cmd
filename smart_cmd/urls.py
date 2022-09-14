from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions, routers

router = routers.SimpleRouter()


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("auth/", include("accounts.urls")),
]
