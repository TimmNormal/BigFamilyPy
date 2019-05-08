from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout

from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

class BlockHelp(FloatLayout):
	def __init__(self,type,deadline,description,title,avatar,**kwargs):
		super(BlockHelp,self).__init__(**kwargs)
		
		self.size_hint_y = None
		self.height = 150
		self.background_color = [.94,.94,.94,1]
		self.add_widget(Button(background_color = [.94,.94,.94,1], background_normal = "",background_down = ""))
		
		avatarImage = AsyncImage(source = avatar,pos_hint = {"x":0,"top":1},size_hint = [.2,.2],allow_stretch = True, keep_ratio = False)
		titleText = Label(text = title, pos_hint = {"x":.21,"top":1},size_hint = [.59,.2])
		deadLineButton = Button(text = deadline,pos_hint = {"right":1,"top":1}, size_hint = [.2,.1])
		reputationButton = Button(text = deadline,pos_hint = {"right":1,"top":.8}, size_hint = [.2,.1])
		descriptionText = Label(text = description,size_hint = [.8,.6],pos_hint = {"center_x":.5,"center_y":.5})
		typeButton = Button(text = type, size_hint = [.2,.1], pos_hint = {"x":0,"y":0})

		self.add_widget(avatarImage)
		self.add_widget(titleText)
		self.add_widget(deadLineButton)
		self.add_widget(reputationButton)
		self.add_widget(descriptionText)
		self.add_widget(typeButton)
		
		