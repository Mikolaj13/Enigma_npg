import os
from tkinter import *

class SettingWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Settings")
        ico_path = os.path.join( "Images", "favicon.ico")
        self.iconbitmap(ico_path)

        self.rotor_count = 3
        self.widget_list = WidgetSettingPackList(self)
        Button(text = "Add a rotor",width=12,height=2,command=lambda: self.widget_list.add()).grid(column=4, row=0)
        Button(text="Subtract a rotor", width=12, height=2, command=lambda: self.widget_list.sub()).grid(column=4, row=1)
        Button(text="Reset", width=12, height=2, command=lambda: self.widget_list.reset()).grid(column=5, row=0)
        Button(text="Continue", width=12, height=2, command=lambda: self.cont()).grid(column=5, row=1)


    def get_settings(self):
        return self.widget_list.get()
    def cont(self):
        self.destroy()


class WidgetSettingPack:
    def __init__(self,window,row,col):
        self.setting = 0

        self.plus_button = Button(window,text="+",width=4,height=2,command=lambda: self.plus())
        self.plus_button.grid(row=row,column=col+2)
        self.minus_button = Button(window,text="-",width=4,height=2, command=lambda: self.minus())
        self.minus_button.grid(row=row, column=col)
        self.text_field = Label(window,text="0",width=4,height=2)
        self.text_field.grid(row=row,column=col+1)

    def update(self):
        self.text_field.config(text=str(self.setting))
    def plus(self):
        if self.setting<25:
            self.setting += 1
            self.update()
    def minus(self):
        if self.setting>0:
            self.setting -= 1
            self.update()
    def reset(self):
        self.setting = 0
        self.update()
    def death(self):
        self.plus_button.destroy()
        self.minus_button.destroy()
        self.text_field.destroy()
    def get(self):
        return self.setting

class WidgetSettingPackList:
    def __init__(self,window):
        self.widget_list = []
        self.window = window
        for i in range(2):
            self.widget_list.append(WidgetSettingPack(self.window,i,0))
    def reset(self):
        for i in self.widget_list:
            i.reset()
    def add(self):
        if len(self.widget_list)<5:
            self.widget_list.append(WidgetSettingPack(self.window,len(self.widget_list),0))
    def sub(self):
        if len(self.widget_list)>2:
            self.widget_list[-1].death()
            self.widget_list.pop()
    def get(self):
        return [i.get() for i in self.widget_list]

