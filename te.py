from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle,Line
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.uix.screenmaneger import Screen

class Filter(Widget):
	touchPos = [0,0]
	def __init__(self,**kwargs):

		
		super(Filter,self).__init__(**kwargs)
		radius = Window.width * 0.4
		center_y = Window.height // 2
		center_x = Window.width // 2
		cricleWidth = 50
		with self.canvas:
			Color(.11,.70,.58,1)
			Rectangle(pos = [0,0], size = [Window.width, center_y - radius])
			Rectangle(pos = [0,0], size = [center_x - radius, Window.height])
			Rectangle(pos = [Window.width - ((Window.width//2) - radius),0], size = [(Window.width//2) - radius,Window.height])
			Rectangle(pos = [0,Window.height - (center_y - radius)], size = [Window.width, center_y - radius])
			Line(circle = (center_x,center_y,radius + cricleWidth), width = cricleWidth, close = True)
		

		

class AvaMaker(Screen):
	def __init__(self,**kwargs):
		super(AvaMaker,self).__init__(**kwargs)
		source = "SISe.jpg"
		self.main = FloatLayout()
		self.avatar = Button(background_normal = source,background_down = source,size_hint = [None,None])
		test = Image(source = source)
		self.avatar.size = test.texture_size
		
		self.touchPos = self.avatar.pos
		self.ImageX = self.avatar.x
		self.ImageY = self.avatar.y
		
		self.stratHeight = self.avatar.height
		self.startWidth = self.avatar.width
		
		self.main.add_widget(self.avatar)
		diametr = Window.width * 0.8
		if self.avatar.height < diametr:
			addNum = diametr - self.avatar.height
			self.avatar.size_hint = [None,None]
			self.avatar.height += addNum
			self.avatar.width += addNum
			self.avatar.y = Window.height // 2 - diametr //2

		self.minY = Window.height // 2 + diametr //2 - self.avatar.height
		self.maxY = Window.height // 2 - diametr//2
		self.minX = Window.width // 2 + diametr//2 - self.avatar.width
		self.maxX = Window.width // 2 - diametr//2
		
		
		
		if self.stratHeight < self.avatar.width:
			sliderValue = self.stratHeight - diametr 
		else:
			sliderValue = self.startWidth - diametr
			
		sizeChanger = Slider(min = sliderValue * -1,max = 0, on_touch_move = self.lesses,on_touch_down = self.lesses, size_hint_y = .1,pos_hint = {"x":0,"center_y":.2})
		
		okButton = Button(size_hint = [.3,.07], pos_hint = {"center_x":.5,"center_y": .1}, on_press = self.save)  
		
		self.main.add_widget(okButton,0)
		self.main.add_widget(sizeChanger,0)
		self.main.add_widget(Filter(on_touch_down = self.on_touch_down,on_touch_move = self.on_touch_move),2)
		self.add_widget(self.main)
		
	def on_touch_down(self,istance,touch):
		self.touchPos = touch.pos
		self.ImageX = self.avatar.x
		self.ImageY = self.avatar.y
	
	def on_touch_move(self,istance,touch):
		self.avatar.x = self.ImageX + (touch.pos[0] - self.touchPos[0]) 
		self.avatar.y = self.ImageY + (touch.pos[1] - self.touchPos[1])
		
		if self.avatar.x < self.minX:
			self.avatar.x = self.minX
		elif self.avatar.x > self.maxX:
			self.avatar.x = self.maxX
		if self.avatar.y < self.minY:
			self.avatar.y = self.minY
		elif self.avatar.y > self.maxY:
			self.avatar.y = self.maxY
	def lesses(self,istance,touch):
		diametr = Window.width * 0.8
		self.avatar.size = [self.startWidth + istance.value,self.stratHeight + istance.value * 1.5]
		print(istance.value)
		print()
		print(self.avatar.size)
		self.minY = Window.height // 2 + diametr //2 - self.avatar.height
		self.maxY = Window.height // 2 - diametr//2
		self.minX = Window.width // 2 + diametr//2 - self.avatar.width
		self.maxX = Window.width // 2 - diametr//2
		
				
		if self.avatar.x < self.minX:
			self.avatar.x = self.minX
		elif self.avatar.x > self.maxX:
			self.avatar.x = self.maxX
		if self.avatar.y < self.minY:
			self.avatar.y = self.minY
		elif self.avatar.y > self.maxY:
			self.avatar.y = self.maxY
	def save(self,istance):
		diametr = Window.width * 0.8
		self.main.size_hint = [None,None]
		self.main.size = [diametr,diametr]
		self.main.pos = [Window.width//2 - diametr//2,Window.height // 2 - diametr//2]
		self.main.export_to_png("ava.png")
		self.main.size_hint = [1,1]
if __name__ == "__main__":
	Test().run()