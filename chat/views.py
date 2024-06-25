from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import ChatRoom, Message
from .serializer import MessageSerializer, ChatRoomSerializer

class ChatRoomListCreateView(generics.ListCreateAPIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class WebSocketEndpoint(APIView):
    @swagger_auto_schema(
        operation_description="WebSocket connection endpoint",
        manual_parameters=[
            openapi.Parameter('room_name', openapi.IN_QUERY, description="Chat room name", type=openapi.TYPE_STRING)
        ],
        responses={200: 'WebSocket connection established'}
    )
    def get(self, request, room_name):
        return Response({"message": f"WebSocket connection established for room: {room_name}"})
