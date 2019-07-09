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

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"


class InfoPlate(FloatLayout):
	def __init__(self,text,**kwargs):
		super(InfoPlate,self).__init__(**kwargs)
		self.size_hint_y = None
		self.height = 15
		self.add_widget(Button(text = text, size_hint = [.4,1],background_normal = "images/deadline.png",background_down = "images/deadline.png",color = COLOR["LIGHT"]["MAIN_COLOR"], pos_hint = {"center_x":.5,"center_y":.5}))
		
class ProfileActivity(Screen):
	def __init__(self,getData,**kwargs):
		super(ProfileActivity,self).__init__(**kwargs)
		infoBlock = GridLayout(cols = 1,spacing = 10)
		
		
		imagePlace = FloatLayout(size_hint = [1,None], height = 150)
		
		imagePlace.add_widget(AsyncImage(pos_hint = {"center_x":.5,"center_y":.5}, source = getData["avatar"]))
		
		infoBlock.add_widget(imagePlace)
		infoBlock.add_widget(Label(text = getData["login"], color = COLOR["LIGHT"]["MAIN_COLOR"],size_hint_y = None, height = 10))
		infoBlock.add_widget(InfoPlate(str(getData["reputation"])))
		infoBlock.add_widget(InfoPlate(str(getData["helpNum"])))
		
		
		list = ScrollView()
		
		
		
		layoutList = GridLayout(cols = 1, size_hint_y = None)
		layoutList.bind(minimum_height = layoutList.setter('height'))
		layoutList.add_widget(infoBlock)

		list.add_widget(layoutList)
		self.add_widget(list)
		
	def add_block(self,k):
		pass
		