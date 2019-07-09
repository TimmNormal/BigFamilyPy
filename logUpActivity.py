from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView

import os
import requests

from RES import COLOR

	
		

class AvatarImage(FloatLayout):
	def __init__(self,openImages,resizeble = True,source = "",**kwargs):
		super(AvatarImage,self).__init__(**kwargs)
		
		
		self.Avtar = Image(pos_hint = {"x":.0,"y":.0}, source = source)
		
		if resizeble:
			self.size_hint_y = None
			self.height = self.Avtar.texture_size[1]
		
		self.add_widget(Button(pos_hint = {"x":.0,"y":.0},text = source,color = [0,0,0,0], on_press = openImages, background_color = [1,1,1,0]))
		self.add_widget(self.Avtar)
		
	def changeImage(self,source):	
		self.Avtar.source = source


class ChooseImage(Screen):
	def __init__(self,chooseAvatar,**kwargs):
		super(ChooseImage,self).__init__(**kwargs)
		
		images = []
		for d,k,f in os.walk("images"):
			for i in f:
				# print(f)
				if i.endswith(".png"):
					images.append(d + "\\"[0] + i)
					
		
		mainScroll = ScrollView()
		
		self.main = GridLayout(cols = 1, size_hint_y = None, spacing = 15)
		self.main.bind(minimum_height = self.main.setter("height"))
		mainScroll.add_widget(self.main)
		
		for h in images:
			print(h)
			self.main.add_widget(AvatarImage(source = h,openImages = chooseAvatar))
		self.add_widget(mainScroll)
		
		
		
class MakeAvatar(Screen):
	def __init__(self,**kwargs):
		super(MakeAvatar,source,self).__init__(**kwargs)
		
		

class LogUpActivity(Screen):
	REG = True
	
	def __init__(self,openImages,**kwargs):
		super(LogUpActivity,self).__init__(**kwargs)
		
		Window.clearcolor = COLOR["LIGHT"]["MAIN_COLOR"]
		
		self.main = GridLayout(cols = 1, spacing = 15)
		
		self.widgets = []
		
		self.avatar = AvatarImage(openImages = openImages,resizeble = False)
		
		loginL = FloatLayout(size_hint_y = .2)
		self.login = TextInput(background_normal = "images/backLayout.png",background_active = "images/backLayout.png", size_hint = [.8,1], pos_hint = {"center_x":.5,"y":0},hint_text = "Логин",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		loginL.add_widget(self.login)
		
		realNameL = FloatLayout(size_hint_y = .2)
		realName = TextInput(pos_hint = {"center_x":.5,"y":0},background_normal = "images/backLayout.png",size_hint  = [.8,1],background_active = "images/backLayout.png",hint_text = "Ф.И.О",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		realNameL.add_widget(realName)
		
		numberL = FloatLayout(size_hint_y = .2)
		number = TextInput(pos_hint = {"center_x":.5,"y":0},background_normal = "images/backLayout.png",size_hint  = [.8,1],background_active = "images/backLayout.png",hint_text = "Телефонный номер",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		numberL.add_widget(number)
		
		mailL = FloatLayout(size_hint_y = .2)
		mail = TextInput(pos_hint = {"center_x":.5,"y":0},background_normal = "images/backLayout.png",size_hint  = [.8,1],background_active = "images/backLayout.png",hint_text = "Электронная почта",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		mailL.add_widget(mail)
		
		passwordL = FloatLayout(size_hint_y = .2)
		self.password = TextInput(pos_hint = {"center_x":.5,"y":0},background_normal = "images/backLayout.png",size_hint  = [.8,1],background_active = "images/backLayout.png",hint_text = "Пароль",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		passwordL.add_widget(self.password)
		
		copyPasswordL = FloatLayout(size_hint_y = .2)
		copyPassword = TextInput(pos_hint = {"center_x":.5,"y":0},background_normal = "images/backLayout.png",background_active = "images/backLayout.png",size_hint  = [.8,1],hint_text = "Повторите пароль",hint_text_color = COLOR["LIGHT"]["MAIN_COLOR"])
		copyPasswordL.add_widget(copyPassword)
		
		licenseOk = FloatLayout(size_hint_y = None, height = 20)
		licenseOk.add_widget(CheckBox(pos_hint = {"x":.1,"y":0}, size_hint_x = .2))
		licenseOk.add_widget(Button(pos_hint = {"x":.3,"y":0}, size_hint_x = .5, background_color = [0,0,0,0], color = [1,1,1,1], text = "Лиц. Согл."))
		
		readyButtonL = FloatLayout()
		readyButton = Button(size_hint = [.5,.3], pos_hint = {"center_x":.5,"center_y":.4}, on_press = self.logUp)
		readyButtonL.add_widget(readyButton)
		
		
		self.main.add_widget(Widget(size_hint_y = None, height = 10))
		self.main.add_widget(self.avatar)
		self.main.add_widget(loginL)
		self.main.add_widget(realNameL)
		self.main.add_widget(numberL)
		self.main.add_widget(mailL)
		self.main.add_widget(passwordL)
		self.main.add_widget(copyPasswordL)
		self.main.add_widget(licenseOk)
		self.main.add_widget(readyButtonL)
		
		self.add_widget(self.main)
	def checkLogin(self,istance,focus):
		if not focus:
			if len(istance.text) < 4:
				istance.hint_text += " ()"
				istance.background_normal = "images/backLayoutBad.png"
				self.REG = False
			t = requests.post("", json = {"login":self.login.text})
			if t.json()["answer"] == "N":
				istance.hint_text += "(Такой ник уже существует)"
				istance.background_normal = "images/backLayoutBad.png"
				self.REG = False
	def passwordTrueistance(self,istance,focus):
		if not focus:
			if len(istance.text) < 6:
				istance.hint_text += "(Пароль должен содержать больще 6 символов)"
				istance.background_normal = "images/backLayoutBad.png"
				self.REG = False
				
				
	def passworEquall(self,istance,focus):
		if not focus:
			if istance.text != self.password.text:
				istance.hint_text += " (Пароли долны совпадать)"
				istance.background_normal = "images/backLayoutBad.png"
				self.password.background_normal = "images/backLayoutBad.png"
				self.REG = False
		else:
			istance.background_normal = "images/backLayoutBad.png"
			istance.hint_text = istance.hint_text[:len(istance.hint_text) - len(" (Пароли долны совпадать)")]
	def numberReal(self,istance,focus):
		pass
	def mailRal(self,istance,focus):
		pass
	def logUp(self):
		pass
		