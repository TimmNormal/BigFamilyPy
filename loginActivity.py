# -*- coding: utf-8 -*-

from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image

from RES import COLOR, STRING


LANGUAGE = "RUS"
THEME = "LIGHT"

MAIN_COLOR = [.11,.70,.58,1]


Window.clearcolor = [.11,.70,.58,1]



class LoginActivity(Screen):
	def __init__(self,auth,openLogUp,**kwargs):
		super(LoginActivity,self).__init__(**kwargs)
		
		title = Label(text = "BIG FAMILY", font_size = '50px',pos_hint = {"center_x":.5,"center_y":.85})
		
		self.login = TextInput(size_hint = [.75,.05],
						size = [100,2],
						pos_hint = {"center_x":.5,"center_y":.6},
						hint_text = STRING[LANGUAGE]["LOGIN_INPUT"],
						foreground_color = COLOR[THEME]["BACKGROUND"],
						hint_text_color =  COLOR[THEME]["BACKGROUND"],
						font_size = "16sp",
						background_normal = "images/input.png",
						background_active = "images/input.png")
		self.password = TextInput(size_hint = [.75,.05],
								size = [100,20],
								pos_hint = {"center_x":.5,"center_y":.45}, 
								hint_text = STRING[LANGUAGE]["PASSWORD_INPUT"], 
								foreground_color = COLOR[THEME]["BACKGROUND"],
								hint_text_color = COLOR[THEME]["BACKGROUND"],
								background_normal = "images/input.png",
								background_active = "images/input.png",
								password = True)
		
		buttonIn = Button(size_hint = [None,None],
						pos_hint  = {"center_x":.5,"top":.35},
						size = [90,40],text = STRING[LANGUAGE]["LOGIN"],
						color = COLOR[THEME]["MAIN_COLOR"],
						background_color = COLOR[THEME]["BACKGROUND"],
						background_normal = "",
						border = [25,25,25,25],
						on_press = auth) 
		
		logo = Image(source = "images/logo.png",
					pos_hint = {"center_x": .5,"top":.2},
					size_hint = [None,None],
					size = [75,75])
					
		logUpLink = Button(size_hint = [.8,None],
							text = "Еще не с нами? Зарегестрируйся!",
							size = [100,10], 
							pos_hint = {"center_x":.5,"y":.03},
							background_color = [1,1,1,0],
							background_normal = "",
							on_press = openLogUp)
		
		main = FloatLayout()
		main.add_widget(title)
		main.add_widget(self.login)
		main.add_widget(self.password)
		main.add_widget(buttonIn)
		main.add_widget(logo)
		main.add_widget(logUpLink)
		
		self.add_widget(main)