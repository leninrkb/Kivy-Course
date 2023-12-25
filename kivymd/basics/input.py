from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_builder = """
MDTextField:
    hint_text : "Username"
    pos_hint : {"center_x":.5, "center_y":.5}
    size_hint_x : None
    width : 300
    helper_text : "Enter your username"
    icon_right : "account"
    icon_right_color : app.theme_cls.primary_color
"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Cyan"
        screen = Screen()
        # 
        username = Builder.load_string(username_builder)
        # 
        screen.add_widget(username)
        return screen

MainApp().run()