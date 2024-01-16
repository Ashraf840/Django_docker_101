from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json


class homePageConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super(homePageConsumer, self).__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room_name_normalized = None
    
    def connect(self):
        print("Connected to websocket!")
        self.room_group_name = 'homePage_socket'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        async_to_sync(self.accept())
    
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(f"Receives a data {data}!")

    def disconnect(self, *args, **kwargs):
        async_to_sync (self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print("Disconnected from websocket!")