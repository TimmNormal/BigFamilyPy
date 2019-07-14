from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import requests

from RES import COLOR, STRING
from blockHelo import BlockHelp


LANGUAGE = "RUS"
THEME = "LIGHT"


def antyNull(data,type = "str"):
    if data != None:
        return data
    elif type == "int":
        return 0
    else:
        return "None"
    

class MainActivity(Screen):
    def __init__(self,moreInformation,**kwargs):
        self.moreInformation = moreInformation
        self.filterList = {"filter":"none"}
        super(MainActivity,self).__init__(**kwargs)
        list = ScrollView(on_scroll_stop = self.scrol)
        
        self.layoutList = GridLayout(cols = 1, size_hint_y = None, spacing = 15)
        self.layoutList.bind(minimum_height = self.layoutList.setter('height'))
        
        # for g in range(10):
            # layoutList.add_widget(Button(size_hint_y = None,height = 300))
        
        list.add_widget(self.layoutList)
        self.add_widget(list)
        self.updateBlocks()
        
    def addBlock(self,block):
        self.layoutList.add_widget(block,len(self.layoutList.children))
        # self.layoutList.add_widget(Button(size_hint_y = None,height = 15, background_normal = "images/sshadow.png"))
        
    def scrol(self,istance,k):
        scroll = istance.scroll_y
        if scroll <= 0:
            self.appendBlocks()
        elif scroll >1:
            self.updateBlocks()
            
    def updateBlocks(self):
        try:
            r = requests.post("http://timmcool.pythonanywhere.com/getBlock",json = {"ok":"ok"})
            f = r.json()
            print(r.json())
            self.layoutList.clear_widgets()
            try:
                for b in f:
                    self.layoutList.add_widget(BlockHelp(type = b["Type"],deadline = "DeadLine",reputation = str(b["Reputation"]),description = b["Content"],title = b["Name"],avatar = b["Avatar"],id = int(b["Id"]),userId = int(b["UserId"]),login = b["Login"],moreInformation = self.moreInformation))
            except Exception as e:
                print(e)
            self.lastBlockid = int(f[9]["Id"])
            print(f[9]["Id"])
        except Exception as e:
            print(e)
    def appendBlocks(self):
        try:
            r = requests.post("http://timmcool.pythonanywhere.com/appendBlock",json = {"lastId":self.lastBlockid})
            f = r.json()
            print("________________________JSON_______________________")
            print(r.json())
            try:
                for b in f:
                    self.layoutList.add_widget(BlockHelp(type = b["Type"],deadline = "DeadLine",reputation = str(b["Reputation"]),description = b["Content"],title = b["Name"],avatar = b["Avatar"],id = int(b["Id"]),userId = int(b["UserId"]),moreInformation = self.moreInformation))
            except Exception as e:
                print(e)
        except Exception:
            pass