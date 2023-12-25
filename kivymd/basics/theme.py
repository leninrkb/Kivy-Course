from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark"
        # 
        screen = Screen()
        button = MDRectangleFlatButton()
        # 
        button.text = "I LOVE SANA SUNOMIYA"
        button.pos_hint = {"center_x":.5, "center_y":.5}
        # 
        screen.add_widget(button)
        return screen
    
MainApp().run()