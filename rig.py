from kivy.app import App


from kivy.uix.button import Button

class Riag(App):
	def build(self):
		return Button(text = "0", on_press = self.addR)
		
	def addR(self,istance):
		istance.text = str(int(istance.text) + 1)
		
if __name__ == "__main__":
	Riag().run()