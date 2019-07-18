# -*- coding: utf-8 -*-


from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import BorderImage
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget

from kivy.core.window import Window

from RES import COLOR, STRING

import requests

LANGUAGE = "RUS"
THEME = "LIGHT"


TYPES = ["Транспорт","Финансы","Физ. помощь"]


class ChangeType(Screen):
    typeList = []
    
    def __init__(self,add_type,**kwargs):
        super(ChangeType,self).__init__(**kwargs)
        
        typeScroll = ScrollView()
        
        typeLayout = GridLayout(cols = 1, size_hint_y = None)
        typeLayout.bind(minimum_height = typeLayout.setter("height"))
        
        for t in TYPES:
            typeLayout.add_widget(Button(size_hint_y = None,
                                         height = 50, 
                                         text = t, 
                                         on_press = add_type,
                                         background_normal = "images/backLayout.png",
                                         background_down = "images/backLayout.png"))
        
            
        typeScroll.add_widget(typeLayout)
        
        self.add_widget(typeScroll)
            
class chekText(FloatLayout):
    def __init__(self,text,state = "normal",**kwargs):
        super(chekText,self).__init__(**kwargs)
        
        self.add_widget(CheckBox(size_hint = [.2,.2],group = "imortant",state = state, pos_hint = {"x":0,"center_y":.5}))
        self.add_widget(Label(size_hint = [.7,1], pos_hint = {"right":1}, text = text, color = COLOR["LIGHT"]["MAIN_COLOR"]))

class horin(FloatLayout):
    def __init__(self,**kwargs):
        super(horin,self).__init__(**kwargs)        
        

        self.size_hint = [.8,None]
        self.height = 40
        # self.size_hint_y = .05
        self.add_widget(Button(background_normal = "images/backLayout.png", size_hint = [1,1],pos_hint = {"center_x":.5,"y":0}))
        
        self.add_widget(Label(text = "Время:",size_hint = [.3,1],color = COLOR["LIGHT"]["MAIN_COLOR"],pos_hint = {"x":0,"y":0}))
        self.timeInput = TextInput(size_hint = [.2,.8], pos_hint = {"center_x":.5,"center_y":.5}, multiline = False,background_normal = "images/deadLine.png",background_active = "images/deadLine.png",on_text_validate = self.stoped)
        self.timeInput.bind(focus = self.update)
        # self.timeInput.bind(text = self.stoped)
        self.add_widget(self.timeInput)
        self.deadline = Label(size_hint = [.2,1],pos_hint = {"right":.9,"y":0},color = COLOR["LIGHT"]["MAIN_COLOR"])
        
        self.add_widget(self.deadline)
        
    def stoped(self,istance,state):
        print("ggg")
        if len(istance.text) >=4:
            istance.text = istance.text[:5]
            self.update(istance,False)
        
    
    def update(self,istance,value):
        if not value:
            deadline = self.timeInput.text
            if len(deadline) < 4:
                for i in range(4 - len(deadline)):
                    deadline = deadline + "0"
            
            deadline = deadline[:2] + ":" + deadline[2:5]
            
            self.timeInput.text = deadline
            self.deadline.text = deadline
            istance.focus = False
    
        
class check(FloatLayout):
    def __init__(self,text,group,**kwargs):
        super(check,self).__init__(**kwargs)
        self.important = "Средняя"
        self.size_hint = [.8,None]
        self.height = 50
        
        os = FloatLayout(size_hint = [.95,1], pos_hint = {"center_x":.5,"y":0})
        
        os.add_widget(Button(background_normal = "images/backLayout.png", size_hint = [1,1], pos_hint = {"center_x":.5,"y":0}))
        
        os.add_widget(Label(text = text + ":", color = COLOR["LIGHT"]["MAIN_COLOR"],size_hint = [.28,1], pos_hint = {"x":0,"y":0}, font_size = "12px"))
        
        states = GridLayout(rows = 1, pos_hint = {"right":.95,"y":0}, size_hint = [.73,1])
        
        states.add_widget(CheckBox(group = group))
        states.add_widget(Label(text = "Низкая", font_size = "12px", color = COLOR["LIGHT"]["MAIN_COLOR"]))
        states.add_widget(CheckBox(group = group, state = "down"))
        states.add_widget(Label(text = "Средняя", font_size = "12px", color = COLOR["LIGHT"]["MAIN_COLOR"]))
        states.add_widget(CheckBox(group = group))
        states.add_widget(Label(text = "Высокая", font_size = "12px", color = COLOR["LIGHT"]["MAIN_COLOR"]))
        
        os.add_widget(states)
        
        self.add_widget(os)
    def changeImportant(self,istance):
        self.important = istance.text
        
        
class addImage(ScrollView):
    def __init__(self,**kwargs):
        super(addImage,self).__init__(**kwargs)
        
        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = 50
        
        self.pos_hint = {"x":0,"top":1}
        
        list = GridLayout(rows = 1, size_hint_x = None,spacing = 2)
        list.bind(minimum_width = list.setter('width'))
        
        for b in range(6):
            list.add_widget(Button(size_hint = [None,None], size = [50,50],background_normal = "images/backLayout.png", text = "+", font_size = "25px", color = COLOR["LIGHT"]["MAIN_COLOR"]))


        
        self.add_widget(list)
        

class chooseTime(FloatLayout):


    def __init__(self,**kwargs):
        super(chooseTime,self).__init__(**kwargs)
        
        
        hours = ScrollView(pos_hint = {"x":0,"top":0})
        minutes = ScrollView(pos_hint = {"right":1,"y":0})
        
        wid = 100
                
        Mlist = GridLayout(cols = 1, size_hint = [None,None], width = wid)
        Mlist.bind(minimum_height = Mlist.setter('height'))
        
        Hlist = GridLayout(cols = 1, size_hint = [None,None], width = wid)
        Hlist.bind(minimum_height = Hlist.setter('height'))        
        
        for m in range(0,61):
            Mlist.add_widget(Button(height = 50, text = str(m)))
            
        for h in range(0,25):
            Hlist.add_widget(Button(height = 50, text = str(h)))
        
        hours.add_widget(Hlist)
        minutes.add_widget(Mlist)
        
        self.add_widget(hours)
        self.add_widget(minutes)





class AddActivity(Screen):
    type = None
    def __init__(self,userId,openChooseType,endsPost,**kwargs):
        super(AddActivity,self).__init__(**kwargs)
        
        self.openChooseType = openChooseType
        self.userId = userId
        
        self.ends = endsPost
        
        self.createWidgets()
        

    

        
    def addPost(self,istance):
        send = True
        data = {}
        
        data["userId"] = self.userId
        data["name"] = self.nameInput.text
        data["type"] = self.type
        data["deadLine"] = self.deadLine.important
        data["important"] = self.important.important
        data["content"] = self.description.text
        
        for k in data.keys():
            if data[k] == None or data[k] == "":
                send = False
                #makeToast("Заполните все поля")
                break
        if send:
            requests.post("http://timmcool.pythonanywhere.com/addBlock",json = data)
            self.clear_widgets()
            self.createWidgets()
            self.ends()
        
        
    def clearActivity(self,istance):
        pass
    def createWidgets(self):
        list = ScrollView()
        
        layoutList = GridLayout(cols = 1, size_hint_y = None,spacing = 5)
        layoutList.bind(minimum_height = layoutList.setter('height'))
        
        
        self.nameInput= TextInput(size_hint = [.8,1],pos_hint = {"center_x":.5,"y":0}, width = 200,background_normal = "images/backLayout.png",background_active = "images/backLayout.png",multiline = False,foreground_color = COLOR["LIGHT"]["MAIN_COLOR"],hint_text = "Название",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
        self.description = TextInput(size_hint = [.8,1],pos_hint = {"center_x":.5,"y":0}, width = 200,background_normal = "images/backLayout.png",background_active = "images/backLayout.png",foreground_color = COLOR["LIGHT"]["MAIN_COLOR"],hint_text = "Описание",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
        
        nameLayout = FloatLayout(size_hint = [1,None], height = 50, pos_hint = {"center_x":.5,"Y":0})
        nameLayout.add_widget(self.nameInput)
        
        descriptionLayout = FloatLayout(size_hint = [1,None], height = 100)
        descriptionLayout.add_widget(self.description)
        
        self.deadLine = check("Срочность","dead")
        
        addImages = FloatLayout(size_hint = [1,None], height = 50)
        addImages.add_widget(addImage())
        
        
        checkCategoryF = FloatLayout(size_hint = [1,None], height = 30)
        self.checkCategory = Button(text = "Выберете категорию", background_normal = "images/button.png", size_hint = [.9,1], pos_hint = {"center_x":.5,"y":0}, on_press = self.openChooseType)
        checkCategoryF.add_widget(self.checkCategory)
        
        endButtons = FloatLayout(size_hint = [.7,None], height = 75)
        okButton = Button(size_hint = [.5,None],height = 30, background_normal = "images/button.png", text = "Пртвердиь", pos_hint = {"center_x":.5,"top":1}, on_press = self.addPost)
        noButton = Button(size_hint = [.3,None],height = 35, background_normal = "images/button.png", text = "Отмена", pos_hint = {"center_x":.5,"y":0}, on_press = self.clearActivity)
        
        self.important = check("Важность","imp")
        
        endButtons.add_widget(okButton)
        endButtons.add_widget(noButton)
        
        layoutList.add_widget(nameLayout)
        layoutList.add_widget(descriptionLayout)
        layoutList.add_widget(self.deadLine)
        layoutList.add_widget(self.important)
        layoutList.add_widget(addImages)
        layoutList.add_widget(Widget(size_hint = [1,None], height = 5))
        layoutList.add_widget(checkCategoryF)
        layoutList.add_widget(Widget(size_hint = [1,None], height = 40))
        layoutList.add_widget(endButtons)

        
        
        list.add_widget(layoutList)
        self.add_widget(list)