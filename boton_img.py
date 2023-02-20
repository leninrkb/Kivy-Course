from kivy.app import App
from kivy.uix.button import Button
from functools import partial
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string(''' 
<Main>:
	Button:
		text:'hola desde builder'
		size_hint:.12,.12
		Image:
			source:'img.png'
			center_x:self.parent.center_x
			center_y:self.parent.center_y
''')

class Main(App, BoxLayout):
	def build(self):
		return self
Main().run()