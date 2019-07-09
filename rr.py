from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import AsyncImage
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.button import Button

from kivy.core.text import Label as CoreLabel


label = """
<BackgroundColor@Widget>
    background_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
# Now you can simply Mix the `BackgroundColor` class with almost
# any other widget... to give it a background.
<BackgroundLabel@Label+BackgroundColor>
    background_color: 1, 1, 0, 1
    # Default the background color for this label
    # to r 0, g 0, b 0, a 0 """

Builder.load_string(label)

# from dopInformationActivity import DopActivity

class MessageBlock(FloatLayout):
	def __init__(self,messageText,**kwargs):
		super(MessageBlock,self).__init__(**kwargs)
		message = CoreLabel(text = messageText,text_size = [Window.width // 2,None], padding = [5.0,3.0])
		message.refresh()
		
		self.add_widget(Button())
		self.add_widget(Image(texture = message.texture))
		self.size_hint = [None,None]
		if message.size[1] <= 21:
			self.size = [len(messageText) * 10,message.size[1]]
		else:
			self.size = message.size
		message.refresh()

		
		



class test(App):
	def build(self):
		main = FloatLayout()
		text = MessageBlock(messageText = "effddd")

		main.add_widget(text)
		return main
	def dele(self):
		self.lay.remove_widget(self.d)
		
if __name__ == "__main__":
	d = test()
	d.run()
	
