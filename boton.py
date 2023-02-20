from kivy.app import App
from kivy.uix.button import Button
from functools import partial

class Main(App):
	def disable(self, instance, *args):
		instance.disable=True
	def update(self, instance, *args):
		instance.text='desabilitado'
	def build(self):
		btn1 = Button(text='click para deshabilitar')
		btn1.bind(on_press=partial(self.disable, btn1))
		btn1.bind(on_press=partial(self.update, btn1))
		return btn1
Main().run()