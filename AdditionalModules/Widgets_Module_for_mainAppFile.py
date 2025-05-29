from tkinter import *

class ButtonIOMaker():
    def __init__(self, row, col, text, window):
        self.window = window

        self.button = Button(window,width=2, height=4 , text=text, bg="light grey")
        self.button.grid(row=row, column=col, rowspan=3)
        self.button.config(state=DISABLED)

    def clicked(self):
        self.button.config(bg="green")
        self.window.after(200, lambda: self.button.config(bg="light grey"))

class TextMaker():
    def __init__(self, row, window, text):
        Label(window, text= text).grid(row=row,columnspan=2)
        self.text = Text(window, height=8,width = 80)

        scroll = Scrollbar(window, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.grid(row=row+1, column=0,columnspan=25, sticky="nsew")
        scroll.grid(row=row+1, column=25, sticky="ns")

        self.text.config(state=DISABLED)

    def typing(self,char):
        self.text.config(state = NORMAL)
        self.text.insert(END,char)
        self.text.config(state= DISABLED)

    def backspace(self):
        self.text.config(state=NORMAL)
        self.text.delete("end-2c", "end-1c")
        self.text.config(state=DISABLED)