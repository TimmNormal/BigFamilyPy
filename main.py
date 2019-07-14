from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

from kivy.clock import Clock

from kivy.config import Config


Config.set("graphics","width",300)
Config.set("graphics","height",600)

Config.write()

import sys

sys.path.append("request/")

from dopInformationActivity import DopActivity
from mainActivity import MainActivity
from profileActivity import ProfileActivity
from settingActivity import SettingActivity
from addActivity import AddActivity, ChangeType
from dialogActivity import DialogActivity
from loginActivity import LoginActivity
from blockHelo import BlockHelp
from logUpActivity import LogUpActivity, ChooseImage
from dialogScreen import DialogScreen
from makeAvatar import AvaMaker
from RES import COLOR, STRING

from kivy.base import EventLoop



from kivy.config import Config
import requests as req
import sqlite3 as db

# Config.set("graphics","fullscreen","fake")
Config.set("graphics","max_height",'630')
Config.set("graphics","max_width",'300')
Config.set("graphics","resizable",1)

MAIN_COLOR = [.11,.70,.58,1]

Config.write()

Window.clear_color = [.85,.85,.85,1]


LANGUAGE = "RUS"
THEME = "LIGHT"

con = db.connect("local.db")
cursor = con.cursor()



cursor.execute("create table if not exists user(id integer, login text, reputation integer,num integer,avatar text)")
cursor.execute("create table if not exists contacts(title text,content text)")

con.commit()    
    


class Up(FloatLayout):
    TITLES = {"mainActivity":"Запросы", "profileActivity":"Профиль","addActivity":"Добавить","dialogActivity":"Сообщения","settingActivity":"Настройки"}
    def __init__(self,**kwargs):
        super(Up,self).__init__(**kwargs)
        self.size_hint_y = None
        self.height = 50
        
        self.title = Label(text = "Запросы",pos_hint = {"x":.05,"center_y":.5}, size_hint_x = .2)
        
        self.add_widget(Shadow(pos_hint = {"center_y":0,"x":0}))
        self.add_widget(Button(pos_hint = {"y":0,"x":0},background_color = COLOR[THEME]["MAIN_COLOR"], color = COLOR[THEME]["BACKGROUND"],background_normal = "",background_down = "",border = [0,0,0,0], size_hint_y = None, height = 70))
        self.add_widget(self.title)
    
    def changeTitle(self,activity):
        if self.title.text == self.TITLES[activity]:
            return False
        else:
            self.title.text = self.TITLES[activity]
            return True
        

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

            

class ToolBar(FloatLayout):
    def __init__(self,change,**kwargs):
        super(ToolBar,self).__init__(**kwargs)
        self.size_hint_y = None    
        self.height = 50
        spacing = 0
        self.add_widget(Button(background_color = COLOR["LIGHT"]["MAIN_COLOR"], background_normal = "",background_down = ""))
        # shadow = Button(background_normal = "",size_hint = [1,None], height = 1, background_color = [0,0,0,1], pos_hint = {"top":1})
        # self.add_widget(shadow)
        size = 35
        self.add_widget(Shadow(pos_hint = {"center_y":.5,"x":0}, inverse = True),2)
        self.add_widget(ToggleButton(size_hint = [None,None], size = [size,size], group = "toolBar", color = [1,1,1,0], text = "mainActivity",on_press = change, border = [1,1,1,1],background_normal = "images/main.png",background_down = "images/mainPress.png", pos_hint = {"center_x":.1,"center_y":.5}, state = "down"))
        self.add_widget(ToggleButton(size_hint = [None,None], size = [size,size], group = "toolBar",color = [1,1,1,0],text = "profileActivity", on_press = change, border = [1,1,1,1],background_normal = "images/profile.png",background_down = "images/profilePress.png",background_color = [1,1,1,1], pos_hint = {"center_x":.3,"center_y":.5}))
        self.add_widget(ToggleButton(size_hint = [None,None], size = [size,size], group = "toolBar",color = [1,1,1,0], text = "addActivity",on_press = change, border = [0,0,0,0],background_normal = "images/add.png",background_down = "images/addPress.png",background_color = [1,1,1,1], pos_hint = {"center_x":.5,"center_y":.5}))
        self.add_widget(ToggleButton(size_hint = [None,None], size = [size,size], group = "toolBar",color = [1,1,1,0], text = "dialogActivity",on_press = change, border = [0,0,0,0],background_normal = "images/dialog.png",background_down = "images/dialogPress.png",background_color = [1,1,1,1], pos_hint = {"center_x":.7,"center_y":.5}))
        self.add_widget(ToggleButton(size_hint = [None,None], size = [size,size], group = "toolBar",color = [1,1,1,0], text = "settingActivity",on_press = change, border = [0,0,0,0],background_normal = "images/gear.png",background_down = "images/gearPress.png",background_color = [1,1,1,1], pos_hint = {"center_x":.9,"center_y":.5}))
        
        
        
class BigFamaly(App):
    BACK_STACK = []
    USER_ID = None

    
    def build(self):
    

        EventLoop.window.bind(on_keyboard = self.back)
        
        self.globalStyle = ScreenManager(transition = NoTransition())
        
        appMain = Screen(name = "app")        
        self.main = ScreenManager(transition = NoTransition(), size_hint_y = None, height = Window.height - 100, pos_hint = {"x":0,"center_y":.5})
        style = FloatLayout()

        # up = FloatLayout(size_hint_y = None, height = 50)
        # up.add_widget(Button(size_hint_y = None, height = 50,background_color = COLOR[THEME]["MAIN_COLOR"], color = COLOR[THEME]["BACKGROUND"],background_normal = "",background_down = "",border = [0,0,0,0]))
        # up.add_widget(Shadow(pos_hint = {"x":0,"center_y":0}))
        
        self.toolBar = ToolBar(change = self.changeActivity)
        self.up = Up(pos_hint = {"x":0,"top":1})
        
        style.add_widget(self.up,0)
        style.add_widget(self.main,1)
        style.add_widget(self.toolBar,0)
        
        appMain.add_widget(style)
        
        self.loginActivity = LoginActivity(name = "login",auth = self.auth,openLogUp = self.openLogUp)
        self.logUpActivity = LogUpActivity(name = "logUp", openImages = self.openImages)

        
        self.globalStyle.add_widget(self.loginActivity)
        self.globalStyle.add_widget(self.logUpActivity)
        self.globalStyle.add_widget(appMain)
        self.globalStyle.add_widget(ChangeType(name = "type",add_type = self.chooseType))
        
        cursor.execute("SELECT id,avatar FROM user")
        self.data = cursor.fetchone()

        if self.data == [] or self.data == None:
            self.globalStyle.current = "login"
        else:  
            self.USER_ID = self.data[0]
            self.loadsActivity()
        return self.globalStyle
        
    def changeActivity(self,istance):
        if self.up.changeTitle(istance.text):
            self.main.current = istance.text
            self.BACK_STACK.append(["app",istance.text])
        else:
            istance.state = "down"
        
    def auth(self,istance):
        try:
            request = {"login":self.loginActivity.login.text,"password":self.loginActivity.password.text,"test":1}
            resp = req.post("http://timmcool.pythonanywhere.com/auth",json = request)
            rJson = resp.json()
            if rJson["Message"] == "222":
                cursor.execute("INSERT INTO user(id,login, reputation, num,avatar) VALUES(?,?,?,?,?)",(rJson["Id"],rJson["Login"],rJson["Reputation"],rJson["NumHelp"],rJson["Avatar"]))
                con.commit()
                self.USER_ID = rJson["Id"]
                self.loadsActivity()
        except Exception:
            #makeToast("Проверьте поджлючение к интернету")
            print("NO INTERNET MAZAFAKA")

            
    def getData(self):
        cursor.execute("SELECT * FROM user")
        data = cursor.fetchone()
        result = {"id":data[0],"login":data[1], "reputation": data[2], "helpNum": data[3],"avatar":data[4]}
        return result
        
    def chooseType(self,type):
        self.addActivity.type = type.text
        self.addActivity.checkCategory.text = type.text
        self.globalStyle.current = "app"
        self.sectorActivity = True
    
    def openChooseType(self,istance):
        self.globalStyle.current = "type"
        self.BACK_STACK.append(["globalStyle","type"])
    
    def moreInformation(self,i):
        self.globalStyle.remove_widget(self.moreInfoActivity)
        
        self.moreInfoActivity = DopActivity(name = "moreInformation",title = i.title,content = i.description,type = i.type,avatar = i.avatar,login = i.login,reputation = i.reputation,deadline = i.deadline,userId = i.userId,selfUserID = self.USER_ID,blockId = i.blockId,openDialog = self.openDialog)
        self.globalStyle.add_widget(self.moreInfoActivity)
        
        self.globalStyle.current = "moreInformation"
        self.BACK_STACK.append(["globalStyle","moreInformation"])
        
    def loadsActivity(self):
        self.globalStyle.current = "app"
        Window.clearcolor = [.96,.96,.96,1]
        
        data = self.getData()
        
        mainActivity = MainActivity(name= "mainActivity", moreInformation = self.moreInformation)
        # mainActivity.addBlock(BlockHelp(type = "Tra",deadline = "23",description = "Help Help Help Help Help Help Help Help Help Help Help BEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH",title = "HEEEEEELP", avatar = "http://timmcool.pythonanywhere.com/SIS.jpg"
        self.dialogScreen = DialogScreen(0,0,0,0)
        self.moreInfoActivity = DopActivity(title = "",content = "",type = "",avatar = "",login = "",reputation = "",deadline = "",userId = "",selfUserID = "",blockId = "",openDialog = self.openDialog)
        
        
        profileActivity = ProfileActivity(name = "profileActivity",getData = data)

        self.addActivity = AddActivity(name = "addActivity",userId  = self.USER_ID,openChooseType = self.openChooseType)
        dialogActivity = DialogActivity(name = "dialogActivity",openDialog = self.openDialog)
        
        
        settingActivity = SettingActivity(name = "settingActivity",userId  = self.USER_ID, exit = self.exit)
        
        self.BACK_STACK.append(["app","mainActivity"])
        
        
        self.main.add_widget(mainActivity)
        self.main.add_widget(profileActivity)
        self.main.add_widget(self.addActivity)
        self.main.add_widget(dialogActivity)
        self.main.add_widget(settingActivity)
        
    def back(self,window,key,*largs):
        if key == 27:
            self.BACK_STACK = self.BACK_STACK[:-1]
            if self.BACK_STACK !=[]:
                inverseBack = self.BACK_STACK[-1:]
                if inverseBack[0][0] == "app":
                    self.globalStyle.current = "app"
                    self.main.current = inverseBack[0][1]
                    self.up.changeTitle(inverseBack[0][1])
                    for w in self.toolBar.children:
                        try:
                            if w.text == inverseBack[0][1]:     
                                w.state = "down"
                            else:
                                w.state = "normal"
                        except Exception:
                            continue
                elif inverseBack[0][0] == "globalStyle":
                    self.globalStyle.current = inverseBack[0][1]
                return True
            else:
                return False

    
    def openDialog(self,i):
        self.globalStyle.remove_widget(self.dialogScreen)
        
        self.dialogScreen.setParametrs(i.idTo,i.idFrom,i.blockName,i.userName)
        self.globalStyle.add_widget(self.dialogScreen)
        
        self.globalStyle.current = "dialog"
        self.BACK_STACK.append(["globalStyle","dialog"])
        
        
    def openLogUp(self,istance):
        self.globalStyle.current = "logUp"
        if ["globalStyle","login"] not in self.BACK_STACK:
            self.BACK_STACK.append(["globalStyle","login"])
        self.BACK_STACK.append(["globalStyle","logUp"])
        
    def openImages(self,istance):    
        self.globalStyle.add_widget(ChooseImage(name = "choser",chooseAvatar = self.chooseImage))
        self.globalStyle.current = "choser"
        
    def chooseImage(self,istance):
        print(self.globalStyle.children)
        print()
        try:
            self.globalStyle.remove_widget(avaMaker)
        except Exception:
            print("LooooL")
        print(self.globalStyle.children)
        
        avaMaker = AvaMaker(name = "avaMaker",source = istance.text)
        self.globalStyle.add_widget(avaMaker)
        self.globalStyle.current = "avaMaker"

        
    def exit(self,istance):
        cursor.execute("DROP TABLE user")
        con.commit()
        Window.clearcolor = COLOR["LIGHT"]["MAIN_COLOR"] 
        self.globalStyle.current = "login"
        
        
    # def exit(self,istance):
        # cursor.execute("DROP TABLE user")
        # cursor.commit()
        # self.globalStyle.current = "login"
        
if __name__ == "__main__":
    BigFamaly().run()