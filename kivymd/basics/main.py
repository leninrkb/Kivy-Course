from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon


class MainApp(MDApp):
    def build(self):
        label = MDLabel()
        icon = MDIcon(icon="heart") 
        # 
        label.text = "I love Sana Sunomiya"
        label.theme_text_color = "Custom"
        label.text_color = (133/255, 100/255, 10/255, 1)
        label.halign = "center"
        label.bold = True
        label.font_style = "H1"
        # 
        return label
    
MainApp().run()