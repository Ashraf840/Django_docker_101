from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(('personApp.urls', 'app_name'), namespace="PersonApplication")),
]
