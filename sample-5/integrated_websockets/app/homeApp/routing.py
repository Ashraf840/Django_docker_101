from django.urls import path
from .consumers import homePageConsumer


websocket_urlpatterns = [
    path('ws/homepage/', homePageConsumer.as_asgi()),
]