from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

class InformationButton(Button):
	def __init__(self,type,deadline,reputation,description,title,avatar,userId,id,**kwargs):
		super(InformationButton,self).__init__(**kwargs)
		self.size_hint = [.3,.1]
		self.pos_hint = {"right":.97,"y":.03}
		self.background_down = "images/button.png"
		self.background_normal = "images/button.png"
		self.text = "Перейти"
		
		self.type = type
		self.deadline = deadline
		self.reputation = reputation
		self.description = description
		self.title = title
		self.avatar = avatar
		self.userId = userId
		self.blockId = id

class testImage(Button):
	def __init__(self,**kwargs):
		super(testImage,self).__init__(**kwargs)
		self.background_color = [1,1,1,0]
		with self.canvas:

			Color(1,0,0,1)
			Line(ellipse = (None,None,self.height,self.width), pos_hint = {"x":0,"y":0})

class CricleImage(FloatLayout):
	def __init__(self,source,size,**kwargs):
		super(CricleImage,self).__init__(**kwargs)
		self.size_hint = [None,None]
		self.size = size
		self.add_widget(AsyncImage(source = source, pos_hint = {"x":0,"y":0}))
		self.add_widget(Button(pos_hint = {"x":0,"y":0},background_color = [1,1,1,1], background_normal = "images/cricleFilter.png",background_down = "images/cricleFilter.png"))
		

class BlockHelp(FloatLayout):
	MID_REPUTATION = 5000
	def __init__(self,type,deadline,reputation,description,title,avatar,id,userId,moreInformation,**kwargs):
		super(BlockHelp,self).__init__(**kwargs)
		
		MAX_CHARS = 30
		MAX_ROWS = 10
		

		iReputation = int(reputation)	
		
		if iReputation < self.MID_REPUTATION//2:
			reputation_color = [.78,.16,.20,1]
		elif iReputation > self.MID_REPUTATION * 1.5:
			reputation_color = [.36,.78,.15,0]
		else:
			reputation_color = [78,.77,0,1]
			
		self.size_hint_y = None
		self.height = 600
		self.background_color = [.94,.94,.94,1]
		
		background = GridLayout(cols = 1)
	
		
		self.add_widget(Button(background_color = [1,1,1,1], background_normal = "images/block.png",background_down = "images/block.png",pos_hint = {"x":0,"y":0}))
		
		
		avatarImage =  AsyncImage(pos_hint =  {"x":.02,"top":.97}, size_hint = [None,None], size = [60,60], source = avatar) #CricleImage(source = avatar,size = [60,60], pos_hint = {"x":.02,"top":.97})
								
		titleText = Label(text = title, pos_hint = {"x":.21,"top":1},size_hint = [.59,.2], color = COLOR["LIGHT"]["MAIN_COLOR"])
		
		
		
		deadLineButton = Button(text = deadline,
								pos_hint = {"x":0,"top":1}, 
								size_hint = [1,.4],
								size = [80,20],
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								color = COLOR["LIGHT"]["TEXT_COLOR"])
		reputationButton = Button(text = reputation,
								pos_hint = {"x":0,"y":0},
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								size_hint = [1,.4],
								size = [80,20],
								color = reputation_color
								)
								
		infoLayout = FloatLayout(size_hint = [.2,.25], 
					size = [80,50],
					pos_hint = {"right":.98,"top":.97})
					
		infoLayout.add_widget(reputationButton)
		infoLayout.add_widget(deadLineButton)
		

		
		
		descriptionText = Label(text = description,size_hint = [.8,.6],pos_hint = {"center_x":.5,"center_y":.5}, max_lines = 1, color = COLOR["LIGHT"]["MAIN_COLOR"])
		descriptionText.text_size = [Window.width * 0.8,None]
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
		self.add_widget(InformationButton(on_press = moreInformation,type = type,deadline = deadline,reputation = reputation,description = description,title = title,avatar = avatar,userId = userId,id = id))
		
		