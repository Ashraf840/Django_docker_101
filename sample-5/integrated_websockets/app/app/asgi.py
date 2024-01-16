import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import homeApp.routing as home_r

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = ProtocolTypeRouter(
    {
        # Just HTTP for now. (We can add other protocols later.)
        "http": get_asgi_application(),
        #"http": django_asgi_app,     # TESTING
        'websocket': AuthMiddlewareStack(
            URLRouter(
                home_r.websocket_urlpatterns
            ),
        ),
    }
)