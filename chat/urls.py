from django.urls import path
from .views import ChatRoomListCreateView, MessageListCreateView, WebSocketEndpoint

urlpatterns = [
    path('api/rooms/', ChatRoomListCreateView.as_view(), name='chat_rooms'),
    path('api/messages/', MessageListCreateView.as_view(), name='messages'),
    path('ws/chat/<str:room_name>/', WebSocketEndpoint.as_view(), name='websocket_endpoint'),
]
