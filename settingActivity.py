from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget
from kivy.core.window import Window

import sqlite3 as db
import requests

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

TEXT_COLOR = {"VK":[0,0,1,1],"OK":[1,1,0,1],"FB":[0,0,1,1],"DC":[.5,.5,0,1],"Any":COLOR["LIGHT"]["MAIN_COLOR"]}

con = db.connect("local.db")
cursor = con.cursor()

# cursor.execute("SELECT id FROM user")
USER_ID = 1#cursor.fetchone()[0]




class SwitchT(ToggleButton):
    STATES = {"down":"T","normal":"F"}
    def __init__(self,type,**kwargs):
        super(SwitchT,self).__init__(**kwargs)
        try:
            stateResp = requests.post("http://timmcool.pythonanywhere.com/getState",json = {"userId":USER_ID})
            realStates = stateResp.json()
            if realStates[type] == "T":
                self.state = "down"
            else:
                self.state = "normal"
        except Exception:
            self.state = "normal"
        
        self.background_normal = "images/SwitchOff.png"
        self.background_down = "images/SwitchOn.png"
        
        self.on_press = self.changeState
        self.type = type
        
    def changeState(self):
        state = self.STATES[self.state]
        reponse = requests.post("http://timmcool.pythonanywhere.com/changeState", json = {"param":self.type,"state":state,"userId":USER_ID})
        print(self.type,state,USER_ID)

class TitleButton(Button):
    def __init__(self,**kwargs):
        super(TitleButton,self).__init__(**kwargs)
        self.background_down = ""
        self.background_normal = "" 
        self.text = "Категория"
        self.background_color = COLOR["LIGHT"]["MAIN_COLOR"]
        self.size_hint = [None,None]
        self.size = [self.width,30]

class AnyInput(FloatLayout):
    def __init__(self,openTypes,**kwargs):
        super(AnyInput,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 30
        self.text = ""
        self.content = TextInput(size_hint_x = .8,pos_hint = {"right":1,"y":0}, on_text_validate = self.textSetter,background_normal = "images/deadline.png",background_active = "images/deadline.png",border = [0,0,0,0], multiline = False)
        self.content.bind(focus = self.whiter)
        
        self.add_widget(Button(size_hint_x = .2,on_press = openTypes, pos_hint = {"x":0,"y":0}, background_down = "",background_normal = "",background_color = COLOR["LIGHT"]["MAIN_COLOR"]))
        self.add_widget(self.content)
    def textSetter(self,istance):
        self.text = istance.text
    def whiter(self,istance,state):
        if state:
            istance.background_color = [1,1,1,1]

class SpecialButton(Button):
    
    def __init__(self,type,**kwargs):
        super(SpecialButton,self).__init__(**kwargs)
        self.type = type
        self.background_down = ""
        self.background_normal = ""
        self.background_color = TEXT_COLOR[type]   
        
class ChagerType(GridLayout):
    TYPES = [["Вконтакте","VK"],["Однк","OK"],["FaceBook","FB"],["Discord","DC"],["Другое","Any"]]
    
    def __init__(self,**kwargs):
        super(ChagerType,self).__init__(**kwargs)
        self.cols = 1
        self.spacing = 3
        self.title = TitleButton(on_press = self.moreChange)
        self.add_widget(self.title)
        self.close = True
        self.type = None
        
    def moreChange(self,istance):
        self.clears(istance,close = self.close)
        if self.close:
            for t in self.TYPES:
                self.add_widget(SpecialButton(text = t[0], type = t[1], on_press = self.setType, size_hint  = [None,None],size = self.title.size))
        self.close = not self.close
    def setType(self,istance):
        if istance.type != "Any":
            self.clear_widgets()
            self.title = TitleButton(on_press = self.moreChange)
            self.title.background_color = istance.background_color
            self.title.text = istance.text
            

        else:
            self.clear_widgets()
            self.title = AnyInput(self.moreChange)
            
        self.moreChange(istance)
        self.type = istance.type
        
    def clears(self,istance,close = True):
        self.clear_widgets()
        self.add_widget(self.title)
        self.close = close
        
class MessageBox(FloatLayout):
    def __init__(self,title,delWidget,addContact,**kwargs):
        super(MessageBox,self).__init__(**kwargs)
        
        self.add_widget(Button(background_normal = "",background_down = "",background_color = [.5,.5,.5,.5],on_press = delWidget))
        mainWindow = FloatLayout(size_hint = [.9,.3],pos_hint = {"center_x":.5,"center_y":.5})
        self.typeChanger = ChagerType(size_hint = [.4,.15],pos_hint = {"x":.08,"center_y":.6})
        
        titlePlate = Button(size_hint_y = .2,pos_hint = {"x":0,"top":1}, text = title, background_down = "",background_normal = "",background_color = COLOR["LIGHT"]["MAIN_COLOR"])
        mainPlate = Button(size_hint_y = .8,pos_hint = {"x":0,"y":0}, background_down = "",background_normal = "",background_color = [.85,.85,.85,1], on_press = self.typeChanger.clears)       
       
        self.dataContact = TextInput(size_hint = [.4,.19],pos_hint = {"x":.5,"center_y":.58},background_normal = "images/deadline.png",background_active = "images/deadline.png", font_size = "12px", border = [0,0,0,0], multiline = False)
        self.dataContact.bind(focus = self.whiter)
        
        readyButton = Button(text = "Ok", background_down = "images/button.png",background_normal = "images/button.png", size_hint = [.5,.25],pos_hint = {"center_x":.5,"y":.1},on_press = addContact)
        
        mainWindow.add_widget(titlePlate)
        mainWindow.add_widget(mainPlate)
        
        mainWindow.add_widget(readyButton)
        mainWindow.add_widget(self.typeChanger)
        mainWindow.add_widget(self.dataContact)

        
        self.add_widget(mainWindow)
    def whiter(self,istance,state):
        if state:
            istance.background_color = [1,1,1,1]
    def zerosInput(self):
        self.dataContact.text = ""
        self.typeChanger.title = TitleButton(on_press = self.typeChanger.moreChange)
        self.typeChanger.clears(None)
        
class MoreContact(FloatLayout):
    def __init__(self,title,content,color = "Any",**kwargs):
        super(MoreContact,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 25
        
        self.add_widget(Button(size_hint_x = .2,text = title,color = TEXT_COLOR[color], pos_hint = {"x":.05,"y":0}, background_normal = "images/deadline.png", background_down = "images/deadline.png"))
        self.add_widget(Button(size_hint_x = .6,pos_hint = {"x":.3,"y":0}, text = content, color = COLOR["LIGHT"]["MAIN_COLOR"], background_normal = "images/deadline.png", background_down = "images/deadline.png"))

        
        

class Contact(FloatLayout):
    def __init__(self,contactName,type,**kwargs):
        super(Contact,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 25
        self.size_hint_x = 1
        
        
        self.add_widget(TextInput(pos_hint = {"center_x":.5,"y":0}, size_hint = [.4,.8],background_normal = "images/deadline.png",background_active = "images/deadline.png"))
        self.add_widget(SwitchT(pos_hint = {"right":.98,"y":0}, size_hint = [.17,None], size = [25,25],type = type))
        self.add_widget(Label(text = contactName, pos_hint = {"x":.08,"center_y":.5}, color = COLOR["LIGHT"]["MAIN_COLOR"], size_hint = [None,None],size  = [20,20],padding = [3.5,5]))      
        
class PasswordLine(FloatLayout):
    def __init__(self,text,**kwargs):
        super(PasswordLine,self).__init__(**kwargs)
        
        self.size_hint_y = None
        self.height = 25
        
        width = 30
        
        self.add_widget(Label(size_hint_x = None, width = width, text = text, pos_hint = {"x":.15,"y":0}, color = COLOR["LIGHT"]["MAIN_COLOR"]))
        self.input = TextInput(size_hint_x = .4,pos_hint = {"right":.8,"y":0}, background_active = "images/deadline.png",background_normal = "images/deadline.png")
        self.add_widget(self.input)

class ViewLine(FloatLayout):
    def __init__(self,text,type,**kwargs):
        super(ViewLine,self).__init__(**kwargs)
        
        self.size_hint_y = None
        self.height = 25
        
        width = 30
        
        self.add_widget(Label(size_hint_x = None, width = width, text = text, pos_hint = {"x":.3,"y":0}, color = COLOR["LIGHT"]["MAIN_COLOR"]))
        self.input = SwitchT(size_hint_x = .17,pos_hint = {"right":.9,"y":0}, type = type)
        self.add_widget(self.input)

class SettingBlockView(GridLayout):
    def __init__(self,title,**kwargs):
        super(SettingBlockView,self).__init__(**kwargs)
        
        self.cols = 1
        self.size_hint_y = None
        self.add_widget(Button(size_hint_y = None, height = 20, text = title,background_color = COLOR["LIGHT"]["MAIN_COLOR"],background_down  ="",background_normal = ""),len(self.children) + 1)
        
        self.add_widget(Widget(size_hint_y = None,height = 10))
        self.add_widget(ViewLine("Отображать ЛД","contactsVis"))
        self.add_widget(Widget(size_hint_y = None,height = 10))
        self.add_widget(ViewLine("Телефонный номер","numberVis"))
        self.add_widget(Widget(size_hint_y = None,height = 10))
        self.add_widget(ViewLine("Почтовый адресс","mailVis"))
        self.heightStability(self)
        



    def heightStability(self,object):
        height = 0
        for c in object.children:
            height += c.height
        object.height = height
        
class SettingBlockPassword(GridLayout):
    def __init__(self,title,**kwargs):
        super(SettingBlockPassword,self).__init__(**kwargs)
        
        self.cols = 1
        self.size_hint_y = None
        self.height = 100
        self.add_widget(Button(size_hint_y = None, height = 20, text = title,background_color = COLOR["LIGHT"]["MAIN_COLOR"],background_down  ="",background_normal = ""),len(self.children) + 1)
        self.middle = GridLayout(cols = 1, size_hint_y = None, height = 300)
        
        self.oldPassword = PasswordLine(text = "Старый пароль")
        self.newPassword = PasswordLine(text = "Новый пароль")
        self.copyPassword = PasswordLine(text = "Повторите")
        
        height = 0
        for h in self.middle.children:
            height += h.height
        self.middle.height = height
        
        self.middle.add_widget(Widget(size_hint_y = None,height = 10))
        self.middle.add_widget(self.oldPassword)
        self.middle.add_widget(Widget(size_hint_y = None,height = 10))
        self.middle.add_widget(self.newPassword)
        self.middle.add_widget(Widget(size_hint_y = None,height = 10))
        self.middle.add_widget(self.copyPassword)
        self.middle.add_widget(Widget(size_hint_y = None,height = 20))
        
        
        addPlate = FloatLayout(size_hint_y = None,height = 13)
        addPlate.add_widget(Button(size_hint = [.35,None], size = [50,50], pos_hint = {"right":.99,"y":0},text = "Подтвердить", background_down = "images/button.png",background_normal = "images/button.png"))
        self.add_widget(self.middle)
        self.add_widget(Widget(size_hint_y = None,height = 25))
        self.add_widget(addPlate)
        
        self.heightStability(self.middle)
        self.heightStability(self)
        
    def heightStability(self,object):
        height = 0
        for c in object.children:
            height += c.height
        object.height = height
        
       
class SettingBlock(GridLayout):
    def __init__(self,title,addMessageBox,**kwargs):
        super(SettingBlock,self).__init__(**kwargs)
        
        self.cols = 1
        self.size_hint_y = None
        self.add_widget(Button(size_hint_y = None, height = 20, text = title,background_color = COLOR["LIGHT"]["MAIN_COLOR"],background_down  ="",background_normal = ""),len(self.children) + 1)
        self.middle = GridLayout(cols = 1, size_hint_y = None, height = 0)
        
        
        addPlate = FloatLayout(size_hint_y = None,height = 50)
        addPlate.add_widget(Button(size_hint = [None,None], size = [50,50], pos_hint = {"right":1,"y":0},text = "+",background_normal = "images/cricle.png",background_down = "images/cricle.png",on_press = addMessageBox))
        self.add_widget(self.middle)
        self.add_widget(Widget(size_hint_y = None,height = 10))
        self.add_widget(addPlate)
        

    def addContact(self, tittle, content,type):
        self.middle.add_widget(Widget(size_hint_y = None,height = 10))
        self.middle.add_widget(MoreContact(tittle,content,type))
        height = 0
        for h in self.middle.children:
            height += h.height
        self.middle.height = height
        self.heightStability()
        
    def heightStability(self):
        height = 0
        for c in self.children:
            height += c.height
        self.height = height
        

class SettingActivity(Screen):
    
    def __init__(self,userId,exit,**kwargs):
        super(SettingActivity,self).__init__(**kwargs)
        list = ScrollView()
        self.messageBox = MessageBox("Доп контакт",self.delWidget,self.addContact)
        self.userId = userId

        
        self.manyContacts = SettingBlock("Доп контакты",self.addMessageBox)
        self.getData()
                
        layoutList = GridLayout(cols = 1, size_hint_y = None, spacing = 10)
        layoutList.bind(minimum_height = layoutList.setter('height'))
		
        contacts = FloatLayout(size_hint_y = None,height = 75)
        contacts.add_widget(Contact("Телефон","numberVis", pos_hint = {"center_x":.5,"top":.9}))
        contacts.add_widget(Contact("E-MAIL","mailVis", pos_hint = {"center_x":.5,"y":.1}))
        
        
        layoutList.add_widget(Widget(size_hint_y = None,height = 10))
        
        
        layoutList.add_widget(contacts)
        
        
        # for g in range(10):
            # layoutList.add_widget(SettingBlock("jkj"))
        
        layoutList.add_widget(self.manyContacts)
        layoutList.add_widget(SettingBlockPassword("Смена пароля"))
        layoutList.add_widget(SettingBlockView("Конфедициальность"))
        
        layoutList.add_widget(Button(size_hint_y = None, height = 50, text = "Выйти", color = [1,0,0,1], background_normal = "images/deadline.png",background_down = "images/deadline.png",on_press = exit))
        
        list.add_widget(layoutList)
        
        
        self.add_widget(list)
             
    def addMessageBox(self,istance):
        self.add_widget(self.messageBox)
    def delWidget(self,istance):
        self.remove_widget(self.messageBox)
    def addContact(self,istance):
        while True:
            if self.messageBox.dataContact.text == "":
                self.messageBox.dataContact.background_color = [1,0,0,1]
                break
            if self.messageBox.typeChanger.type == None:
                self.messageBox.typeChanger.title.background_color = [1,0,0,1]
                break
            if self.messageBox.typeChanger.title.text == "":
                self.messageBox.typeChanger.title.content.background_color = [1,0,0,1]
                break
            self.remove_widget(self.messageBox)
            
            self.manyContacts.addContact(self.messageBox.typeChanger.title.text,
                                         self.messageBox.dataContact.text,
                                         self.messageBox.typeChanger.type)
            self.setData(self.messageBox.typeChanger.title.text,
                         self.messageBox.dataContact.text,
                         self.messageBox.typeChanger.type)
            
            self.messageBox.zerosInput()
            break
    
    def getData(self):
        try:
            response = requests.post("http://timmcool.pythonanywhere.com/getContacts", json = {"userId":self.userId})
            responseJs = response.json()
            try:
                responseJs["None"]
            except Exception:
                for c in responseJs:
                    self.manyContacts.addContact(c["Title"],c["Content"],c["Type"])
        except Exception as e:
            print(self.userId)
            print(e)
    def setData(self,title,content,type):
        try:
            response = requests.post("http://timmcool.pythonanywhere.com/setContacts", json = {"title":title,"content": content,"userId":self.userId,"type":type})
            
        except Exception:
            print("LOOOL")
        
        