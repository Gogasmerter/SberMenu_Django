from django.contrib import admin
import django.contrib.auth.urls
from django.urls import include, path

urlpatterns = [
    path("users/", include("users.urls")),
    path("users/", include(django.contrib.auth.urls)),
    path("admin/", admin.site.urls),
]
