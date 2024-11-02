from django.urls import path
from chat.consumers import PersonalChatConsumer

websocket_urlpatterns = [
    path('ws/chat', PersonalChatConsumer.as_asgi())
]