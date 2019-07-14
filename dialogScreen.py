from kivy.uix.screenmanager import Screen
from kivy.core.text import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

from kivy.core.window import Window as Win
from kivy.clock import Clock

import requests

class Message(FloatLayout):
    def __init__(self,message,writer = False,**kwargs):
        super(Message,self).__init__(**kwargs)
        MAX_WIDTH = Win.width // 2
        
        if writer:
            position = {"right": 1,"y":0}
        else:
            position = {"x":0,"y":0}
            
        
        # self.add_widget(Button(size_hint_x = MAX_WIDTH, pos_hint = {"right": 1,"y":0}))
        
        messageText = Label(text = message, padding = [3.0,4.0])
        messageText.refresh()
        if messageText.texture.size[0] <= MAX_WIDTH:
            messageText.text_size = [messageText.texture.size[0],None]
        else:
            messageText.text_size = [MAX_WIDTH,None]
        messageText.refresh()
        print(MAX_WIDTH,messageText.texture.size,messageText.text_size)
        self.add_widget(Button(pos_hint = position, size_hint_x = None, width = messageText.texture.size[0]))
        messageImage = Image(texture = messageText.texture,size_hint_x = None, width = messageText.texture.size[0], pos_hint = position)
        
        self.size_hint_y = None
        self.height = messageText.texture.size[1]
        
        self.add_widget(messageImage)
        
        

class DialogScreen(Screen):
    def __init__(self,idTo,idFrom,helpName,userName,**kwargs):
        super(DialogScreen,self).__init__(**kwargs)
        
        print("From",idFrom)
        self.name = "dialog"
    
        try:
            Clock.unschedule(Clock.schedule_interval(self.getMessage,5))
            print("KILL")
        except Exception:
            print("UNKIL")
        Clock.schedule_interval(self.getMessage,5)
        print(len(Clock.get_events()))


        
        main = BoxLayout(orientation = "vertical")
        messInput = BoxLayout(orientation = "horizontal",size_hint_y = None,height = Win.height * 0.1)
        
        self.textMessage = TextInput(size_hint_x = None, width = Win.width * 0.8)
        messInput.add_widget(self.textMessage)
        messInput.add_widget(Button(size_hint_x = None, width = Win.width * 0.2, on_press = self.sendMessage))
        
        messLine = ScrollView()
        self.messBox = BoxLayout(orientation = "vertical",size_hint_y = None)
        self.messBox.bind(minimum_height = self.messBox.setter("height"))
        messLine.add_widget(self.messBox)
        
        main.add_widget(messLine)
        main.add_widget(messInput)
        self.add_widget(main)
        self.setParametrs(idTo,idFrom,helpName,userName)
        
        

    def sendMessage(self,istance):
        if self.textMessage.text != "":
            send = requests.post("https://TimmCool.pythonanywhere.com/setMessage", json = {"content": self.textMessage.text,"idTo": self.idTo,"idFrom":self.idFrom})
            self.messBox.add_widget(Message(self.textMessage.text,True))
            self.textMessage.text = ""
        
    def getMessage(self,dt,append = "getMessage"):
        getMessage =  requests.post("https://TimmCool.pythonanywhere.com/" + append, json = {"id":self.lastId,"idFrom":self.idFrom,"idTo":self.idTo})
        request = getMessage.json()
        print(request)
        try:
            request["None"]
        except Exception:
            for m in request:
                print(m)
                if int(m["IdFrom"]) == self.idFrom:
                    self.messBox.add_widget(Message(m["Content"],True),len(self.messBox.children))
                    print("ME")
                else: 
                    self.messBox.add_widget(Message(m["Content"],False),len(self.messBox.children))
                    print("NOT ME")
                print("ME ID",self.idFrom)
                    
                self.lastId = int(m["Id"])
        # print("Last ID",self.lastId)
    
    def setParametrs(self,idTo,idFrom,helpName,userName):
        self.idTo = idTo
        self.idFrom = idFrom
        self.blockName = helpName
        self.userName = userName
        self.lastId = 0
        self.messBox.clear_widgets()
        self.getMessage(1,"/getAllMessage")
        