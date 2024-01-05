from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        rows = []
        for i in range(20):
            row = (f"item {i}", f"item {i+1}")
            rows.append(row)
        cols = [("food",dp(30)), ("food",dp(30))]
        table = MDDataTable(
            column_data = cols, 
            row_data = rows,
            check = True,
            elevation = 1
            )
        table.pos_hint = {"center_x":.5, "center_y":.5}
        table.size_hint = (.9, .7)
        table.bind(on_check_press = self.check_press)
        screen.add_widget(table)
        return screen
    
    def check_press(self, dataTable, row:list):
        print("hi")
        print(dataTable)
        print(row)
    
MainApp().run()