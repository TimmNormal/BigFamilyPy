from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Line, Ellipse
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.core.text import Label as Short


from RES import COLOR, STRING

LANGUAGE = "RUS"
THEME = "LIGHT"

class ShortenText(FloatLayout):
    def __init__(self,content,contentSize,**kwargs):
        super(ShortenText,self).__init__(**kwargs)
        texture = Short(text = content, color = COLOR["LIGHT"]["MAIN_COLOR"], text_size = [contentSize[0],None],shorten = True, shorten_from = "right",split_str = "")
        texture.refresh()
        if texture.texture.height < contentSize[1]:
            texture.text_size = texture.texture.size
        else:
            texture.text_size = contentSize
            texture.max_lines = 5

        texture.render()
        texture.refresh()
            
        self.texture = Image(texture = texture.texture,pos_hint = {"x":0,"top":1})
        self.size_hint = [None,None]
        self.size = texture.texture.size
        self.add_widget(self.texture)
        # self.add_widget(Button(pos_hint = {"x":0,"y":0}))

class InformationButton(Button):
	def __init__(self,type,deadline,reputation,description,title,avatar,userId,id,login,**kwargs):
		super(InformationButton,self).__init__(**kwargs)
		self.size_hint = [.3,.15]
		self.pos_hint = {"right":.96,"y":.05}
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
		self.login = login

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
	MID_REPUTATION = 250
	def __init__(self,type,deadline,reputation,description,title,avatar,id,userId,moreInformation,login,**kwargs):
		super(BlockHelp,self).__init__(**kwargs)
		
		MAX_CHARS = 30
		MAX_ROWS = 10
		

		iReputation = int(reputation)	
		
		if iReputation < self.MID_REPUTATION//2:
			reputation_color = [.78,.16,.20,1]
		elif iReputation > self.MID_REPUTATION * 1.5:
			reputation_color = [.36,.78,.15,1]
		else:
			reputation_color = [78,.77,0,1]
			
		self.size_hint_y = None
		self.height = 200
		self.background_color = [.94,.94,.94,1]
		
		background = GridLayout(cols = 1)
	
		
		self.add_widget(Button(background_color = [1,1,1,1], background_normal = "images/block.png",background_down = "images/block.png",pos_hint = {"x":0,"y":0}))
		
		
		avatarImage =  AsyncImage(pos_hint =  {"x":.02,"top":.97}, size_hint = [None,None], size = [60,60], source = avatar) #CricleImage(source = avatar,size = [60,60], pos_hint = {"x":.02,"top":.97})
								
		titleText = Label(text = title, pos_hint = {"x":.21,"top":1},size_hint = [.59,.2], color = COLOR["LIGHT"]["MAIN_COLOR"])
		
		
		
		deadLineButton = Button(text = deadline,
								pos_hint = {"x":0,"top":1}, 
								size_hint = [1,.4],
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								color = COLOR["LIGHT"]["TEXT_COLOR"])
		reputationButton = Button(text = reputation,
								pos_hint = {"x":0,"y":0},
								background_normal = "images/deadline.png",
								background_down = "images/deadline.png",
								size_hint = [1,.4],
								color = reputation_color
								)
								
		infoLayout = FloatLayout(size_hint = [.25,.25], 
					size = [95,60],
					pos_hint = {"right":.96,"top":.95})
					
		infoLayout.add_widget(reputationButton)
		infoLayout.add_widget(deadLineButton)
		

		
		
		descriptionText =  ShortenText(content = description,contentSize = [Window.width * 0.8,self.height * 0.45],pos_hint = {"center_x":.5,"center_y":.4}) #Label(text = description,size_hint = [.8,.6],pos_hint = {"center_x":.5,"center_y":.5}, max_lines = 1, color = COLOR["LIGHT"]["MAIN_COLOR"])
		# descriptionText.text_size = [Window.width * 0.8,None]
		typeButton = Button(text = type,
							size_hint = [None,None],
							size = [90,30],
							pos_hint = {"x":.04,"y":.05}, 
							background_normal = "images/type.png", 
							background_down = "images/type.png",
							color = COLOR["LIGHT"]["TEXT_COLOR"])
							

		self.add_widget(avatarImage)
		self.add_widget(titleText)
		self.add_widget(infoLayout)
		self.add_widget(descriptionText)
		self.add_widget(typeButton)
		self.add_widget(InformationButton(on_press = moreInformation,type = type,deadline = deadline,reputation = reputation,description = description,title = title,avatar = avatar,userId = userId,id = id,login = login))
		
		