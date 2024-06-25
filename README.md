# Chat API Documentation

Welcome to the Chat API documentation. This API allows you to create chat rooms, send messages, and interact with chat rooms using both REST API and WebSockets.

## Features

- Create and list chat rooms
- Send and retrieve messages
- Real-time messaging with WebSockets
- Swagger documentation for REST API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ShohjahonObruyevOybekovich/drf_yasg_websocket_chat.git
    cd chat-api
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r r.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## REST API Endpoints

### List and Create Chat Rooms

- **GET / POST** `/chat/api/rooms/`
- Retrieve a list of chat rooms or create a new chat room.

### List and Create Messages

- **GET / POST** `/chat/api/messages/`
- Retrieve a list of messages or send a new message.

## WebSocket Endpoint

### Connect to a Chat Room

- **WebSocket** `/ws/chat/<room_name>/`
- Connect to a chat room and send/receive messages in real-time.

## Swagger Documentation

For detailed REST API documentation, visit the [Swagger UI](http://127.0.0.1:8000/redoc/).

## Usage

1. Create a chat room using the REST API:
    ```bash
    curl -X POST http://127.0.0.1:8000/chat/api/rooms/ -d "name=Room1"
    ```

2. Send a message using the REST API:
    ```bash
    curl -X POST http://127.0.0.1:8000/chat/api/messages/ -d "content=Hello&room=1"
    ```

3. Connect to a chat room using WebSocket:
    ```javascript
    const chatSocket = new WebSocket('ws://127.0.0.1:8000/ws/chat/Room1/');
    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log(data.user + ': ' + data.message);
    };
    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
    chatSocket.send(JSON.stringify({'message': 'Hello, Room1!'}));
    ```

