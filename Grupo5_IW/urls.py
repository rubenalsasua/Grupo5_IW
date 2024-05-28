from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("appDeustotil_Tech", include("appDeustotil_Tech.urls")),
]
