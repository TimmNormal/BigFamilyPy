from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.text import Label as Text

import requests

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

Window.clearcolor = [.94,.94,.94,1]

class Content(Image):
    def __init__(self,text,**kwargs):
        super(Content,self).__init__(**kwargs)
        
        content = Text(text = text,color = COLOR["LIGHT"]["MAIN_COLOR"],text_size = [Window.width * 0.8,None])
        content.refresh()
        
        self.size_hint = [None,None]
        self.size = content.texture.size
        self.texture = content.texture
        
        


class AllInformation(FloatLayout):
    def __init__(self,title,content,type,**kwargs):
        super(AllInformation,self).__init__(**kwargs)
        self.add_widget(Button(background_normal = "images/block.png",background_down = "images/block.png", pos_hint = {"x":0,"y":0}))
        self.size_hint_y = None
        self.height = 0
        titleButton = Label(text = title,color = COLOR["LIGHT"]["MAIN_COLOR"], font_size = "22px",pos_hint = {"center_x":.5,"top":.97},size_hint = [None,None], size = [30,30])
        contentButton = Content(text = content,pos_hint = {"center_x":.5,"center_y":.5})
        typeButton = Button(text = type,
                        size_hint = [None,None],
                        size = [80,20],
                        pos_hint = {"x":.04,"y":.05}, 
                        background_normal = "images/type.png", 
                        background_down = "images/type.png",
                	  	color = COLOR["LIGHT"]["TEXT_COLOR"])
        self.add_widget(titleButton)
        self.add_widget(contentButton)
        self.add_widget(typeButton)
        
        for c in self.children:
        	self.height += c.height
        
class OkButton(Button):
    def __init__(self,idFrom = 0,idTo = 0,userName = "",blockName = "",blockId = 0,**kwargs):
        super(OkButton,self).__init__(**kwargs)
        self.size_hint = [.5,None]
        self.height = 30 
        self.background_normal = "images/button.png"
        self.pos_hint = {"center_x":.5,"top":1}
        
        self.idFrom = idFrom
        self.idTo = idTo
        self.userName = userName
        self.blockName = blockName
        self.blockId = blockId


class InfoPlate(FloatLayout):
    def __init__(self,text,**kwargs):
        super(InfoPlate,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 15
        self.add_widget(Button(text = text, size_hint = [.4,1],background_normal = "images/deadline.png",background_down = "images/deadline.png",color = COLOR["LIGHT"]["MAIN_COLOR"], pos_hint = {"center_x":.5,"center_y":.5}))
        
class DopActivity(Screen):
    def __init__(self,title,content,type,avatar,login,reputation,deadline,userId,selfUserID,blockId,openDialog,**kwargs):
        super(DopActivity,self).__init__(**kwargs)
        infoBlock = GridLayout(cols = 1,spacing = 10, size_hint_y = None, height = 200)
        
        self.openDialog = openDialog
        self.userId = userId
        self.sUserID = selfUserID
        self.type = type
        self.blockId = blockId
        self.d = selfUserID
        # self.postCreateDialog = postCreateDialog
        
        imagePlace = FloatLayout(size_hint = [1,None], height = 150)
        
        imagePlace.add_widget(AsyncImage(pos_hint = {"center_x":.5,"center_y":.5}, source = avatar))
        
        infoBlock.add_widget(imagePlace)
        infoBlock.add_widget(Label(text = login, color = COLOR["LIGHT"]["MAIN_COLOR"],size_hint_y = None, height = 10))
        infoBlock.add_widget(InfoPlate(reputation))
        infoBlock.add_widget(InfoPlate(deadline))
        endButtons = FloatLayout(size_hint = [.7,None], height = 75)

        
        list = ScrollView()
        
        
        
        layoutList = GridLayout(cols = 1, size_hint_y = None)
        layoutList.bind(minimum_height = layoutList.setter('height'))
        layoutList.add_widget(infoBlock)
        layoutList.add_widget(AllInformation(title = title,content = content,type = type))
        layoutList.add_widget(Widget(size_hint = [1,None],height = 20))
        if userId == selfUserID:
            endButtons.add_widget(OkButton(text = "Редактировать"))
        else:
            okButton = OkButton(text = "Отозаться",
                        	on_press = self.createDialog,
                            idFrom = selfUserID,
                            idTo = userId,
                            userName = login,
                            blockName = title,
                            blockId = blockId)
                        	
            noButton = Button(size_hint = [.3,None],
                                        height = 35, 
                                        background_normal = "images/backLayoutBad.png", 
                                        text = "Жалоба", 
                                        pos_hint = {"center_x":.5,"y":0}, 
                                        on_press = self.sendReport)
                                	
            endButtons.add_widget(okButton)
            endButtons.add_widget(noButton)
        
        layoutList.add_widget(endButtons)
        layoutList.add_widget(Widget(size_hint_y = None,height = 15))
        
        
        list.add_widget(layoutList)
        self.add_widget(list)
        
    def createDialog(self,istance):
        cD = requests.post("http://timmcool.pythonanywhere.com/createDialog",json = {"idTo":self.userId,"idFrom":self.d,"type":self.type,"blockId": self.blockId})
        print(cD.json())
        self.openDialog(istance)
        
    def sendReport(self,istance):
        pass
    def reCreate(self,istance):
        pass
    
        
    