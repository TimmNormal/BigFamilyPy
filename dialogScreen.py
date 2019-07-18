# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.core.text import Label
from kivy.uix.label import Label as L
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton

from kivy.core.window import Window as Win
from kivy.clock import Clock
from RES import COLOR, STRING

import requests

class Shadow(GridLayout):
    def __init__(self,inverse = False,**kwargs):
        super(Shadow,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 30
        
        self.cols = 1
        self.spacing = 0
        if not inverse:
            for t in range(15,25):
                self.add_widget(Button(size_hint = [1,None],height = 1, background_normal = "", background_down = "",background_color = [0,0,0,1/t],text = str(t)))
        else:
            for t in range(15,25):
                self.add_widget(Button(size_hint = [1,None],height = 1, background_normal = "", background_down = "",background_color = [0,0,0,1/t],text = str(t)),len(self.children))

            



class Stars(BoxLayout):
    STARS = 5
    
    def __init__(self,**kwargs):
        super(Stars,self).__init__(**kwargs)
        
        self.pos_hint = {"center_x":.5,"top":.4}
        self.size_hint = [None,None]
        self.height = 48
        self.width = self.height * self.STARS
        self.orientation = "horizontal"
        self.result = 1
        self.setResult(None)
        self.color = [1,1,1,0]
        
        
    def setResult(self,istance = None):
        if istance != None:
            self.result = int(istance.text)
        self.clear_widgets()
        text = 0
        try:
            for s in range(self.result):
                text +=1
                self.add_widget(Button(size_hint_x = None,
                                        width = self.height,
                                        background_down = "images/cricle.png",
                                        background_normal = "images/cricle.png",
                                        text = str(text),
                                        on_press = self.setResult))
        except Exception:
            pass
        try:
            for s in range(self.STARS - self.result):
                text +=1
                self.add_widget(Button(size_hint_x = None,
                                        width = self.height,
                                        background_down = "images/cricle.png",
                                        background_normal = "images/cricle.png",
                                        background_color = [1,1,1,.2],
                                        text = str(text),
                                        on_press = self.setResult))
        except Exception:
            pass
class StopBox(FloatLayout):
    def __init__(self,close,userId,blockId,closeAll,returnDialog,**kwargs):
        super(StopBox,self).__init__(**kwargs)
        
        self.blockId = blockId
        self.userId = userId
        self.state = "good"
        self.closeAll = closeAll
        self.returnDialog = returnDialog
        
        self.add_widget(Button(background_normal = "",
                                background_down = "",
                                background_color = [.5,.5,.5,.5],
                                on_press = close))
        
        self.mainWindow = FloatLayout(size_hint = [.8,.8], pos_hint = {"center_x":.5,"center_y":.5})
        self.mainWindow.add_widget(Button(pos_hint = {"x":0,"y":0},
                                     background_down = "",
                                     background_normal = "",
                                     background_color = [.85,.85,.85,1]))
                                     
        self.mainWindow.add_widget(Button(text = "Звершение просьбы", 
                                     pos_hint = {"x":0,"top":1},
                                     size_hint_y = .1,
                                     background_down = "",
                                     background_normal = "",
                                     background_color = COLOR["LIGHT"]["MAIN_COLOR"]))
           
        self.mainWindow.add_widget(Button(text = "Готово", 
                              background_down = "images/button.png", 
                              background_normal = "images/button.png",
                              size_hint = [.4,.08], 
                              pos_hint = {"center_x":.5,"y":.05},
                              on_press = self.stopProcess))
        self.coment = TextInput(hint_text = "Отзыв об пользователе",
                            size_hint = [.8,.4],
                            pos_hint = {"center_x":.5,"top":.85},
                            background_normal = "images/backLayout.png",
                            background_active = "images/backLayout.png")
                            
        normal = ToggleButton(size_hint = [.4,.1],
                               pos_hint = {"center_x":.5,"top":.25},
                               background_normal = "images/button.png",
                               background_down = "images/backLayoutBad.png",
                               text = "Хорошо",
                               on_press = self.changeState)
        self.stars = Stars()
        
        self.mainWindow.add_widget(self.stars)     
        self.mainWindow.add_widget(self.coment)     
        self.mainWindow.add_widget(normal)     
                                
                                     
        self.add_widget(self.mainWindow)
    
    def stopProcess(self,istance):
        if self.coment.text == "":
            self.coment.background_normal = "images/backLayoutBad.png"
            return False
        req = requests.post("https://TimmCool.pythonanywhere.com/changeBlockState",json = {"userId":self.userId,"blockId":self.blockId,"coment":self.coment.text,"state":self.state,"stars":self.stars.result})
        print(req.json(),"____",{"userId":self.userId,"blockId":self.blockId,"coment":self.coment.text,"state":self.state,"stars":self.stars.result})
        self.returnDialog()
        self.closeAll()
        
    def changeState(self,istance):
        if istance.state == "down":
            istance.text = "Плохо"
            self.state = "bad"
            self.mainWindow.remove_widget(self.stars)
        else:
            self.state = "good"
            istance.text = "Хорошо"
            self.mainWindow.add_widget(self.stars)
            
class StopMain(GridLayout):
    def __init__(self,stop,**kwargs):
        super(StopMain,self).__init__(**kwargs)
        self.cols = 1
        self.size_hint_x = .4
        self.state = False
        
        self.add_widget(Button(size_hint_y = None,height = 50,text = "Завершить",on_press = stop,background_normal = "images/button.png",background_down = "images/button.png"))

class Up(FloatLayout):

    def __init__(self,name,avatar,openMain,**kwargs):
        super(Up,self).__init__(**kwargs)
        
        self.size_hint_y = None
        self.height = 50
        self.pos_hint = {"x":0,"top":1}
        
        self.readyButton = Button(size_hint = [None,None],size = [self.height,self.height],pos_hint = {"x":0,"y":0},on_press = openMain,background_normal = "images/backLayout.png",background_down = "images/backLayout.png")
        
        self.title = L(text = name,pos_hint = {"center_x":.5,"center_y":.5}, size_hint_x = .2)
        self.avatar = AsyncImage(source = avatar,size_hint = [None,None], pos_hint = {"right":1,"top":1},size = [self.height,self.height])
        
        self.add_widget(Shadow(pos_hint = {"center_y":0,"x":0}),0)
        self.add_widget(Button(pos_hint = {"y":0,"x":0},background_color = COLOR["LIGHT"]["MAIN_COLOR"], color = COLOR["LIGHT"]["BACKGROUND"],background_normal = "",background_down = "",border = [0,0,0,0], size_hint_y = None, height = 70))
        self.add_widget(self.title)
        self.add_widget(self.avatar)
        self.add_widget(self.readyButton)
        


class Message(FloatLayout):
    def __init__(self,message,writer = False,**kwargs):
        super(Message,self).__init__(**kwargs)
        MAX_WIDTH = Win.width // 2
        
        if writer:
            position = {"right": .95,"center_y":.5}
        else:
            position = {"x":.05,"center_y":.5}
            
        
        # self.add_widget(Button(size_hint_x = MAX_WIDTH, pos_hint = {"right": 1,"y":0}))
        
        messageText = Label(text = message, padding = [3.0,4.0],color = COLOR["LIGHT"]["MAIN_COLOR"],font= "20px")
        messageText.refresh()
        if messageText.texture.size[0] <= MAX_WIDTH:
            messageText.text_size = [messageText.texture.size[0],None]
        else:
            messageText.text_size = [MAX_WIDTH,None]
        messageText.refresh()
        print(MAX_WIDTH,messageText.texture.size,messageText.text_size)
        self.size_hint_y = None
        self.height = messageText.texture.size[1]
        
        self.add_widget(Button(pos_hint = position, size_hint = [None,None], width = messageText.texture.size[0] + 4, height = self.height + 2, background_normal = "images/backLayout.png",background_down = "images/backLayout.png",background_color = [.75,.75,.75,1]))
        self.add_widget(Button(pos_hint = position, size_hint_x = None, width = messageText.texture.size[0], background_normal = "images/backLayout.png",background_down = "images/backLayout.png"))
        messageImage = Image(texture = messageText.texture,size_hint_x = None, width = messageText.texture.size[0], pos_hint = position)
        
        
        
        self.add_widget(messageImage)
        
        

class DialogScreen(Screen):
    def __init__(self,idTo,idFrom,helpName,userName,idBlock,avatar,**kwargs):
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

        
        
        self.main = FloatLayout()
        self.messInput = BoxLayout(orientation = "horizontal",size_hint_y = None,height = Win.height * 0.1,pos_hint = {"x":0,"y":0})
        self.up = Up(helpName,avatar,self.openMain)
        self.stopMain = StopMain(self.stop,pos_hint = {"x":0,"top":.91})
        
        self.nonePlate = Button(size_hint_y = .1,background_normal = "",background_down = "",background_color = COLOR["LIGHT"]["MAIN_COLOR"],text = "Завершено")
        
        self.textMessage = TextInput(size_hint_x = None, width = Win.width * 0.8, background_normal = "images/block.png",background_active = "images/block.png")
        self.messInput.add_widget(self.textMessage)
        self.messInput.add_widget(Button(size_hint_x = None, width = Win.width * 0.2, on_press = self.sendMessage,background_normal = "images/button.png",background_down = "images/button.png",text = ">"))
        

        self.messLine = ScrollView(size_hint_y = None, height = Win.height - self.up.height - self.messInput.height - 10,pos_hint = {"x":0,"top":.9})
        self.messBox = BoxLayout(orientation = "vertical",size_hint_y = None,spacing = 5)
        self.messBox.bind(minimum_height = self.messBox.setter("height"))
        self.messLine.add_widget(self.messBox)
        
        self.main.add_widget(self.up,0)
        self.main.add_widget(self.messLine,1)
        self.main.add_widget(self.messInput,0)
        self.add_widget(self.main)
        self.setParametrs(idTo,idFrom,helpName,userName,idBlock,avatar,"",0,None)
        
    def openMain(self,istance):
        if  not self.stopMain.state:
            self.main.add_widget(self.stopMain,0)
        else:
            self.main.remove_widget(self.stopMain)
        self.stopMain.state = not self.stopMain.state
    def stop(self,istance):
        try:
            self.main.add_widget(self.stopBox)
        except Exception:
            self.main.remove_widget(self.stopBox)
            
    def sendMessage(self,istance):
        if self.textMessage.text != "":
            print(self.idTo,self.idFrom,self.blockId)
            send = requests.post("https://TimmCool.pythonanywhere.com/setMessage", json = {"content": self.textMessage.text,"idTo": self.idTo,"idFrom":self.idFrom,"blockId":self.blockId})
            self.messBox.add_widget(Message(self.textMessage.text,True))
            self.textMessage.text = ""
        self.messLine.scroll_y = 0
    def getMessage(self,dt,append = "getMessage"):
        getMessage =  requests.post("https://TimmCool.pythonanywhere.com/" + append, json = {"id":self.lastId,"idFrom":self.idFrom,"idTo":self.idTo,"blockId":self.blockId})
        request = getMessage.json()
        
        print(request,"Last",self.lastId)
        try:
            request["None"]
        except Exception:
            for m in request:
                print(m)
                if int(m["IdFrom"]) == self.idFrom:
                    self.messBox.add_widget(Message(m["Content"],True))
                    print("ME")
                else: 
                    self.messBox.add_widget(Message(m["Content"],False))
                    print("NOT ME")
                print("ME ID",self.idFrom)
                    
                self.lastId = int(m["Id"])
        self.messLine.scroll_y = 0
        # print("Last ID",self.lastId)
    def getMessageAll(self,dt,append = "getMessageAll"):
        try:
            getMessage =  requests.post("https://TimmCool.pythonanywhere.com/" + append, json = {"id":self.lastId,"idFrom":self.idFrom,"idTo":self.idTo,"blockId":self.blockId})
            request = getMessage.json()
            print(request,"Last",self.lastId)
        except Exception:
            request = []
        
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
        try:            
            self.lastId = int(request[0]["Id"])
        except Exception:
            self.lastId = 0
        print("Start",self.lastId)
        

    def closeAll(self):
        try:
            self.main.remove_widget(self.stopBox)
        except Exception:
            pass
        try:
            self.main.remove_widget(self.stopMain)
        except Exception:
            pass
    def setParametrs(self,idTo,idFrom,helpName,userName,blockId,avatar,state,realId,returnDialog):
        print("ID TO",idTo)
        print("ID FROM",idFrom)
        self.idTo = idTo
        self.idFrom = idFrom
        self.blockName = helpName
        self.userName = userName
        self.lastId = 0
        self.blockId = blockId
        self.avatar = avatar
        self.up.title.text = helpName
        self.up.avatar.source = avatar
        self.messBox.clear_widgets()
        self.stateD = state
        self.stopBox = StopBox(self.stop,self.idTo,self.blockId,self.closeAll,returnDialog)
        self.up.readyButton.background_color = [1,1,1,0] if realId != idFrom else [1,1,1,1]
        if state != "active":
            try:
                self.main.add_widget(self.nonePlate)
            except Exception:
                pass
            self.up.readyButton.background_color = [1,1,1,0]
        else:
            try:
                self.main.remove_widget(self.nonePlate)
            except Exception:
                pass
        
        
        self.closeAll()
                
        self.getMessageAll(1,"/getAllMessage")
        