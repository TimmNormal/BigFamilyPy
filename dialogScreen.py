from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label


class Message

class Up(FloatLayout):
	def __init__(self,title,**kwargs):
		super(Up,self).__init__(**kwargs)
		self.size_hint_y = None
		self.height = 50
		
		self.title = Label(text = title,pos_hint = {"x":.05,"center_y":.5}, size_hint_x = .2)
		
		self.add_widget(Shadow(pos_hint = {"center_y":0,"x":0}))
		self.add_widget(Button(pos_hint = {"y":0,"x":0},background_color = COLOR[THEME]["MAIN_COLOR"], color = COLOR[THEME]["BACKGROUND"],background_normal = "",background_down = "",border = [0,0,0,0], size_hint_y = None, height = 70))
		self.add_widget(self.title)

class DialogScreen(Screen):
	def __init__(self,**kwargs):
		super(DialogScreen,self).__init__(**kwargs)
		main = GridLayout(rows = 3)
		
		messageScroll = ScrollView()
		messageList = GridLayout(size_hint_y = None)
		messageList.bind(minimum_height = messageList.setter("height"))
		
		
		
		
		main.add_widget(Up(""))
		