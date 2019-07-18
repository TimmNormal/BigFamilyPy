# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage,Image
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.text import Label as Short


from kivy.core.window import Window

import requests

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

class ShortenText(FloatLayout):
    def __init__(self,content,contentSize,color = COLOR["LIGHT"]["MAIN_COLOR"],font_size = 20,**kwargs):
        super(ShortenText,self).__init__(**kwargs)
        texture = Short(text = content, color = color, text_size = [contentSize[0],None],shorten = True, shorten_from = "right",split_str = "",font_size = font_size)
        texture.refresh()
        if texture.texture.height < contentSize[1]:
            texture.text_size = texture.texture.size
        else:
            texture.text_size = contentSize
            texture.max_lines = 5

        texture.render()
        texture.refresh()
            
        self.texture = Image(texture = texture.texture,pos_hint = {"x":0,"top":1})
        self.size_hint = [None,None]
        self.size = texture.texture.size
        self.add_widget(self.texture)

class BackgroundButton(Button):
    def __init__(self,idFrom,idTo,blockId,name,nameQuest,avatar,stateD,real,**kwargs):
        super(BackgroundButton,self).__init__(**kwargs)
        self.pos_hint = {"x":0,"y":0}
        self.background_color = [0,0,0,0]
        
        self.idTo = idTo
        self.idFrom = idFrom
        self.blockName = nameQuest
        self.userName = name
        self.blockId = blockId
        self.avatar = avatar
        self.stateD = stateD
        self.realId = real


class DialogMain(FloatLayout):
    STATE_COLORS = {"good":[0,1,0,1],"bad":[1,0,0,1],"active":[[0,0,0,0]]}
    def __init__(self,avatar,name,nameQuest,lastMessage,type,lastDate,idFrom,idTo,blockId,stateD,real,openDialog,**kwargs):
        super(DialogMain,self).__init__(**kwargs)
        
        self.size_hint_y = None
        self.height = 75
        
        self.idTo = idTo
        self.idFrom = idFrom
        self.blockName = nameQuest
        self.userName = name
        self.blockId = blockId

        
        self.add_widget(BackgroundButton(idFrom,idTo,blockId,name,nameQuest,avatar,stateD,real, on_press = openDialog))
        self.add_widget(AsyncImage(size_hint_x = None, width = self.height, source = avatar, pos_hint = {"top":1,"x":0}))
        self.add_widget(ShortenText(pos_hint = {"x":.3,"top":1}, content = name,contentSize = [100,30]))
        self.add_widget(ShortenText(pos_hint = {"top":1,"right":1},contentSize = [100,30], content = nameQuest))
        self.add_widget(ShortenText(pos_hint = {"center_y":.5}, x = self.height + 48, contentSize = [100,30], content = lastMessage, color = [83,83,83,1], font_size = 15))
        self.add_widget(Button(text = type,
                                pos_hint = {"right":.98,"y":.02}, 
                                size_hint = [None,None],
                                size = [80,20],
                                background_normal = "images/deadline.png",
                                background_down = "images/deadline.png",
                                color = COLOR["LIGHT"]["TEXT_COLOR"]))
        self.add_widget(Label(size_hint = [None,None], size = [30,30], pos_hint = {"y": .02}, x = self.height + 10, color = [.83,.83,.83,1], text = lastDate))
        self.add_widget(Label(size_hint = [None,None], size = [30,30], pos_hint = {"right":.9,"center_y": .5}, x = self.height + 10, color = self.STATE_COLORS[stateD], text = stateD))
class Line(Label):
    def __init__(self,**kwargs):
        super(Line,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 1
        
        text = ""
        for i in range(Window.width // 8):
            text = text + "_"
        
        self.text = text
        self.color = [.83,.83,.83,1]

        
        # self.add_widget(Button(size_hint = [.8,1], pos_hint = {"center_x":.5,"top":1}))

class DialogActivity(Screen):
    def __init__(self,userId,openDialog,**kwargs):
        super(DialogActivity,self).__init__(**kwargs)
        list = ScrollView(on_scroll_stop = self.updateDialogs)
        self.openDialog = openDialog
        self.userId = userId
        
        self.layoutList = GridLayout(cols = 1, size_hint_y = None, spacing = 15)
        self.layoutList.bind(minimum_height = self.layoutList.setter('height'))
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU","sdsdsdsdsddds","транспоаа","12.12.12")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        # self.addDialog("http://timmcool.pythonanywhere.com/cricle.png","Lol","UUUUU")
        self.getDialogs(userId)
        list.add_widget(self.layoutList)
        self.add_widget(list)
    
    def updateDialogs(self,istance,k):
        scroll = istance.scroll_y
        if scroll > 1:
           self.getDialogs(self.userId)
    
    def addDialog(self,avatar = "", name = "", nameQuest = "",lastMessage = "", type = "",lastDate = "",idFrom = 0,idTo = 0,blockId = 0,stateD = "",real = 0):
        self.layoutList.add_widget(DialogMain(avatar,name,nameQuest,lastMessage,type,lastDate,idFrom,idTo,blockId,stateD,real,self.openDialog))
        self.layoutList.add_widget(Line())
    def getDialogs(self,userId):
        try:
            try:
                self.layoutList.clear_widgets()
            except Exception:
                pass
            print(userId)
            request = requests.post("http://timmcool.pythonanywhere.com/getDialogs",json = {"userId":userId})
            reqJs = request.json()
            print(reqJs)
            try:
                for d in reqJs:
                    self.addDialog(d["Avatar"],d["Login"],d["NameQuest"],d["LastMessage"],d["Type"],"-----------",int(d["IdFrom"]),int(d["IdTo"]),int(d["BlockId"]),d["State"],int(d["RealId"]))
            except Exception as e:
                print(e,"<--------------------DIALOGBLYA")
        except Exception:
            print("None internet")