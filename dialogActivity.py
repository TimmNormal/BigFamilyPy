from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color



from kivy.core.window import Window

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

class DialogMain(FloatLayout):
	def __init__(self,avatar,name,nameQuest,lastMessage,type,lastDate,id,openDialog,**kwargs):
		super(DialogMain,self).__init__(**kwargs)
		
		self.size_hint_y = None
		self.height = 75
		
		self.idUs = id
		
		self.add_widget(Button(pos_hint = {"x":0,"y":0}, background_color = [0,0,0,0], on_press = openDialog))
		self.add_widget(AsyncImage(size_hint_x = None, width = self.height, source = avatar, pos_hint = {"top":1,"x":0}))
		self.add_widget(Label(pos_hint = {"top":1}, x = self.height + 10,size_hint = [None,None], size = [30,30], text = name, color = COLOR["LIGHT"]["MAIN_COLOR"], font_size = "20px"))
		self.add_widget(Label(pos_hint = {"top":1,"right":1},size_hint = [None,None], size = [100,30], text = nameQuest, color = COLOR["LIGHT"]["MAIN_COLOR"], font_size = "20px"))
		self.add_widget(Label(pos_hint = {"center_y":.5}, x = self.height + 48,size_hint = [None,None], size = [30,30], text = lastMessage, color = [83,83,83,1], font_size = "15px"))
		self.add_widget(Button(text = type,
								pos_hint = {"right":.98,"y":.02}, 
								size_hint = [None,None],
								size = [80,20],
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								color = COLOR["LIGHT"]["TEXT_COLOR"]))
		self.add_widget(Label(size_hint = [None,None], size = [30,30], pos_hint = {"y": .02}, x = self.height + 10, color = [.83,.83,.83,1], text = lastDate))
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
	def __init__(self,openDialog,**kwargs):
		super(DialogActivity,self).__init__(**kwargs)
		list = ScrollView()
		self.openDialog = openDialog
		
		
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
		
		list.add_widget(self.layoutList)
		self.add_widget(list)
		
	def addDialog(self,avatar = "", name = "", nameQuest = "",lastMessage = "", type = "",lastDate = "",id = 0):
		self.layoutList.add_widget(DialogMain(avatar,name,nameQuest,lastMessage,type,lastDate,id,self.openDialog))
		self.layoutList.add_widget(Line())
		