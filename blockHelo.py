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
		self.height = 175
		self.background_color = [.94,.94,.94,1]
		self.add_widget(Button(background_color = [1,1,1,1], background_normal = "images/block.png",background_down = "images/block.png",pos_hint = {"x":0,"y":0}))
		
		
		avatarImage = AsyncImage(source = avatar,
								pos_hint = {"x":.02,"top":.97},
								size_hint = [None,None],
								size = [60,60],
								allow_stretch = True, 
								keep_ratio = False)
								
		titleText = Label(text = title, pos_hint = {"x":.21,"top":1},size_hint = [.59,.2])
		
		
		
		deadLineButton = Button(text = deadline,
								pos_hint = {"x":0,"top":1}, 
								size_hint = [None,None],
								size = [80,20],
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								color = COLOR["LIGHT"]["TEXT_COLOR"])
		reputationButton = Button(text = deadline,
								pos_hint = {"x":0,"y":0}, 
								size_hint = [None,None],
								size = [80,20])
								
		infoLayout = FloatLayout(size_hint = [None,None], 
					size = [80,50],
					pos_hint = {"right":.98,"top":.97})
					
		infoLayout.add_widget(reputationButton)
		infoLayout.add_widget(deadLineButton)
		
		descriptionText = Label(text = description,size_hint = [.8,.6],pos_hint = {"center_x":.5,"center_y":.5})
		typeButton = Button(text = type,
							size_hint = [None,None],
							size = [80,20],
							pos_hint = {"x":.02,"y":.03}, 
							background_normal = "images/type.png", 
							background_down = "images/type.png",
							color = COLOR["LIGHT"]["TEXT_COLOR"])

		self.add_widget(avatarImage)
		self.add_widget(titleText)
		self.add_widget(infoLayout)
		self.add_widget(descriptionText)
		self.add_widget(typeButton)
		
		