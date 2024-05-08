from django.urls import path
from .views import PersonPageView

app_name = 'personApp'

urlpatterns = [
    path("", PersonPageView.as_view(), name="PersonPageView"),
]
