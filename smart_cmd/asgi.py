import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from core.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smart_cmd.settings")


application = ProtocolTypeRouter(
    {"http": get_asgi_application(), "websocket": AuthMiddlewareStack(URLRouter(websocket_urlpatterns))}
)
