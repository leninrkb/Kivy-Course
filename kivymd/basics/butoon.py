from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        button = MDFlatButton()
        rectangleButton = MDRectangleFlatButton()
        iconButton = MDIconButton()
        actionButton = MDFloatingActionButton()
        # 
        button.text = "Say Hello!"
        button.pos_hint = {"center_x": .5, "center_y": .5}
        # 
        rectangleButton.text = "Click to hack NASA"
        rectangleButton.pos_hint = {"center_x": .5, "center_y": .4}
        # 
        iconButton.icon = "heart"
        iconButton.pos_hint = {"center_x": .5, "center_y": .3}
        # 
        actionButton.icon = "android"
        actionButton.pos_hint = {"center_x": .5, "center_y": .2}
        # 
        screen.add_widget(button)
        screen.add_widget(rectangleButton)
        screen.add_widget(iconButton)
        screen.add_widget(actionButton)
        return screen
    
MainApp().run()