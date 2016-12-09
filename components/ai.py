# -*- coding: utf-8 -*-
import requests
import json
from meya import Component

url = 'https://console.api.ai/api/query'

payload =
{
  "q": "what is upgrad?",
  "timezone": "2016-12-09T17:40:38+0530",
  "lang": "en",
  "sessionId": "66253e1f-1c2b-4b01-b2f8-6020f922669e",
  "resetContexts": false
}


headers =
{
"v": 20150910,
"accessToken" : "29ae50f9b7494eefb4aadd2d4b069fa9"
"Authorization" : "Bearer dcc5662977b247098c3f4993d5d4d1f1",
"Content-Type" : "application/json;charset=UTF-8"
}



class Ai(Component):
    """post query to Api.ai and prints response"""

    def start(self):
        data = requests.post(url, data=json.dumps(payload), headers=headers)
        print(data.content)
        text = data['id']['result']['speech']

        message = self.create_message(text=text)
        return self.respond(message=message, action="next")
