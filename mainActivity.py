from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

from RES import COLOR, STRING


LANGUAGE = "RUS"
THEME = "LIGHT"

class MainActivity(Screen):
	def __init__(self,**kwargs):
		super(MainActivity,self).__init__(**kwargs)
		list = ScrollView()
		
		self.layoutList = GridLayout(cols = 1, size_hint_y = None)
		self.layoutList.bind(minimum_height = self.layoutList.setter('height'))
		
		# for g in range(10):
			# layoutList.add_widget(Button(size_hint_y = None,height = 300))
		
		list.add_widget(self.layoutList)
		self.add_widget(list)
		
	def addBlock(self,block):
		self.layoutList.add_widget(block)