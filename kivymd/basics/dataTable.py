from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        rows = []
        for i in range(50):
            row = (f"item {i}", f"item {i+1}")
            rows.append(row)
        cols = [("food",dp(30)), ("food",dp(30))]
        table = MDDataTable(column_data = cols, row_data = rows)
        table.pos_hint = {"center_x":.5, "center_y":.5}
        table.size_hint = (.9, .7)
        screen.add_widget(table)
        return screen
    
MainApp().run()