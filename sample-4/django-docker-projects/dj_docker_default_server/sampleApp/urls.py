from django.urls import path
from .views import samplePageView

app_name = "user_auth_urls"

urlpatterns = [
    path("", samplePageView.as_view(), name="samplePageView.index"),
]
