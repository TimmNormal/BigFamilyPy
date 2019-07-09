from kivy.app import App

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

Window.clearcolor = [1,1,1,1]

class Sha(Widget):
	def __init__(self,**kwargs):
		super(Sha,self).__init__(**kwargs)
		
		with self.canvas:
			Color(0,0,0,1)
			Rectangle(size = [300,10], pos = self.pos)
			
		
class Shadow(App):
	def build(self):
		f = FloatLayout()
		g = GridLayout(cols = 1, spacing = 0)
		for t in range(0):
			g.add_widget(Button(size_hint = [1,None],height = .7, background_normal = "", background_down = "",background_color = [0,0,0,1]))
	
		for t in range(15,25):
			g.add_widget(Button(size_hint = [1/t,None],height = .7, background_normal = "", background_down = "",background_color = [0,0,0,1/t],text = str(t)))
		
		f.add_widget(g)
		f.add_widget(Button(size_hint = [1,None],height = 7, pos_hint = {"top":1,"x":0},background_normal = "", background_down = "",background_color = [1,0,0,1]))
		
		return f
		
		
if __name__ == "__main__":
	Shadow().run()