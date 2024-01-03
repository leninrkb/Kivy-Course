from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import IconLeftWidget, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder


list_helper = """
Screen:
    ScrollView:
        MDList:
            id:simple_list
"""

class SimpleListApp(MDApp):
    def build(self):
        screen = Builder.load_string(list_helper)
        return screen
    
    def on_start(self):
        for i in range(10):
            item = OneLineListItem()
            item.text = "Sunomiya = Love"
            self.root.ids.simple_list.add_widget(item)
        return super().on_start()

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        list = MDList()
        scroll = ScrollView()
        for i in range(25):
            icon = ImageLeftWidget()
            icon.source = "./assets/sunomiya1.png"
            item = ThreeLineAvatarListItem()
            item.tertiary_text = "My world"
            item.secondary_text = "My love"
            item.text = "I love Sunomiya"
            item.add_widget(icon)
            list.add_widget(item)
        scroll.add_widget(list)
        screen.add_widget(scroll)
        return screen
            
    
    
# MainApp().run()
SimpleListApp().run()