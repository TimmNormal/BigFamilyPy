from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Point, Rectangle
from kivy.core.window import Window
from kivy.clock import Clock




class WaterWid(Widget):
	def __init__(self,**kwargs):
		super(WaterWid,self).__init__(**kwargs)
		self.points = []
		h = 300
		k = 10
		s = Window.width // k
		f = 0
		for i in range(k + 1):
			self.points.append(f)
			self.points.append(h)
			f+=s
		 
		
		
		with self.canvas:
			Color(1,1,1,1)
			Line(points = self.points)

		

class Water(App):
	def build(self):
		return WaterWid()
		
if __name__ == "__main__":
	Water().run()