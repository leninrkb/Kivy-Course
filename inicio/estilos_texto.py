from kivy.app import App
from kivy.uix.label import Label

class Main(App):
	def build(self):
		return Label(text='[color=79d368][b] texto de prueba [/b][/color] texto normal [i][color=e4e863] mas texto [/color][/i]',markup=True)
Main().run()