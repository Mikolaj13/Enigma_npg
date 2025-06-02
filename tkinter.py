from tkinter import *
#Zarys kalsy setting
class SettingApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Rotor Settings")

        self.rotor_count = 3
        self.widget_list = WidgetSettingPackList(self)
        Button(text = "add a rotor",width=12,height=2,command=lambda: self.widget_list.add()).grid(column=4, row=0)
        Button(text="subtract a rotor", width=12, height=2, command=lambda: self.widget_list.sub()).grid(column=4, row=1)
        Button(text="reset", width=12, height=2, command=lambda: self.widget_list.reset()).grid(column=5, row=0)
        Button(text="continue", width=12, height=2, command=lambda: self.cont()).grid(column=5, row=1)
