from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from helpers import hpusername


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        screen = Screen()
        button = MDFlatButton()
        # 
        button.text = "Show"
        button.pos_hint = {"center_x": .5, "center_y": .4}
        button.on_release = self.showUsername
        # 
        self.username = Builder.load_string(hpusername)
        # 
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def showUsername(self):
        close = MDFlatButton(text="Close")
        close.on_release = self.closeDialog
        self.dialog = MDDialog(buttons=[close])
        self.dialog.title = "This is your username"
        self.dialog.text = self.username.text
        self.dialog.open()
    
    def closeDialog(self):
        self.dialog.dismiss()
        
        

MainApp().run()