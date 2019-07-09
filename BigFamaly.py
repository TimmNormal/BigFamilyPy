from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage

from mainActivity import MainActivity
from profileActivity import ProfileActivity
from settingActivity import SettingActivity
from addActivity import AddActivity
from dialogActivity import DialogActivity
from loginActivity import LoginActivity
from blockHelo import BlockHelp
from RES import COLOR, STRING

from kivy.config import Config
import requests as req
import sqlite3 as db

# Config.set("graphics","fullscreen","fake")
Config.set("graphics","max_height",'630')
Config.set("graphics","max_width",'300')
Config.set("graphics","resizable",1)

MAIN_COLOR = [.11,.70,.58,1]

Config.write()

Window.clear_color = [1,1,1,1]


LANGUAGE = "RUS"
THEME = "LIGHT"

con = db.connect("local.db")
cursor = con.cursor()

cursor.execute("create table if not exists user(id integer, login text)")

con.commit()	




class ToolBar(GridLayout):
	def __init__(self,change,**kwargs):
		super(ToolBar,self).__init__(**kwargs)
		self.rows = 1
		self.cols = 5
		self.spacing = 0
		self.size_hint_y = None
		self.height = 50
		
		spacing = 0
		
		
		
		self.add_widget(ToggleButton(size_hint = [.2,None], height = self.height, group = "toolBar", color = [1,1,1,0], text = "mainActivity",on_press = change, border = [1,1,1,1],background_normal = "images/home.png",background_down = "",background_color = [1,1,1,1]))
		self.add_widget(ToggleButton(size_hint = [.2,None], height = self.height, group = "toolBar",color = [1,1,1,0],text = "profileActivity", on_press = change, border = [1,1,1,1],background_normal = "iamges/profile.png",background_down = "",background_color = [1,1,1,1]))
		self.add_widget(ToggleButton(size_hint = [.2,None], height = self.height, group = "toolBar",color = [1,1,1,0], text = "addActivity",on_press = change, border = [0,0,0,0],background_normal = "images/add.png",background_down = "",background_color = [1,1,1,1]))
		self.add_widget(ToggleButton(size_hint = [.2,None], height = self.height, group = "toolBar",color = [1,1,1,0], text = "dialogActivity",on_press = change, border = [0,0,0,0],background_normal = "images/dialog.png",background_down = "",background_color = [1,1,1,1]))
		self.add_widget(ToggleButton(size_hint = [.2,None], height = self.height, group = "toolBar",color = [1,1,1,0], text = "settingActivity",on_press = change, border = [0,0,0,0],background_normal = "",background_down = "",background_color = [1,1,1,1]))

class BigFamaly(App):

	def build(self):
		self.globalStyle = ScreenManager(transition = NoTransition())
		
		appMain = Screen(name = "app")
		
		self.main = ScreenManager(transition = NoTransition())
		style = GridLayout(cols = 1, rows = 3)
		
		mainActivity = MainActivity(name= "mainActivity")
		mainActivity.addBlock(BlockHelp(type = "Tra",deadline = "23",description = "Help Help Help Help Help Help Help Help Help Help Help",title = "HEEEEEELP", avatar = "http://timmcool.pythonanywhere.com/cricle.png"))
		mainActivity.addBlock(BlockHelp(type = "Tra",deadline = "23",description = "Help Help Help Help Help Help Help Help Help Help Help",title = "HEEEEEELP", avatar = "http://timmcool.pythonanywhere.com/cricle.png"))
		mainActivity.addBlock(BlockHelp(type = "Tra",deadline = "23",description = "Help Help Help Help Help Help Help Help Help Help Help",title = "HEEEEEELP", avatar = "http://timmcool.pythonanywhere.com/cricle.png"))
		mainActivity.addBlock(BlockHelp(type = "Tra",deadline = "23",description = "Help Help Help Help Help Help Help Help Help Help Help",title = "HEEEEEELP", avatar = "http://timmcool.pythonanywhere.com/cricle.png"))

		
		profileActivity = ProfileActivity(name = "profileActivity")
		addActivity = AddActivity(name = "addActivity")
		dialogActivity = DialogActivity(name = "dialogActivity")
		settingActivity = SettingActivity(name = "settingActivity")
		
		
		self.main.add_widget(mainActivity)
		self.main.add_widget(profileActivity)
		self.main.add_widget(addActivity)
		self.main.add_widget(dialogActivity)
		self.main.add_widget(settingActivity)
		style.add_widget(Button(size_hint_y = None, height = 50, background_color = COLOR[THEME]["MAIN_COLOR"], color = COLOR[THEME]["BACKGROUND"],background_normal = "",background_down = "",border = [0,0,0,0]))
		style.add_widget(self.main)
		style.add_widget(ToolBar(change = self.changeActivity))
		
		appMain.add_widget(style)
		
		self.loginActivity = LoginActivity(name = "login",auth = self.auth)
		
		self.globalStyle.add_widget(self.loginActivity)
		self.globalStyle.add_widget(appMain)
		
		cursor.execute("SELECT * FROM user")
		data = cursor.fetchall()
		print(data)
		if data == []:
			self.globalStyle.current = "login"
		else:
			Window.clearcolor = [1,1,1,1]
			self.globalStyle.current = "app"
			
		return self.globalStyle
		
	def changeActivity(self,istance):
		self.main.current = istance.text
	def auth(self,istance):
		request = {"login":self.loginActivity.login.text,"password":self.loginActivity.password.text,"test":1}
		resp = req.post("http://timmcool.pythonanywhere.com/auth",json = request)
		rJson = resp.json()
		if rJson["Message"] == "222":
			cursor.execute("INSERT INTO user(id,login) VALUES(?,?)",(rJson["Id"],rJson["Login"]))
			con.commit()
			self.globalStyle.current = "app"
			Window.clearcolor = [1,1,1,1]
		
		
if __name__ == "__main__":
	BigFamaly().run()