# myapp/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from constructor.genaircs import GVModel

model = GVModel()
class SkillConsumer(WebsocketConsumer):
    async def connect(self):
        
        self.accept()


    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print('text_data_json:', text_data_json)
        message = text_data_json["message"]
        rcs_type =text_data_json["rcs_type"]
        print('message:', message, rcs_type)
        resp = model.get_response(message=message, rcs_type=rcs_type)
        print('resp: ', resp)
        self.send(text_data=json.dumps({"message": resp}))

# class SkillConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         message = data["message"]
#         # Send the result back to the client
#         await self.send(text_data=json.dumps({"result": "message recieved", "message": message}))

