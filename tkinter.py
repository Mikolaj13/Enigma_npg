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
