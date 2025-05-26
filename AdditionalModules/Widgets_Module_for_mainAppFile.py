from tkinter import *

class TextMaker():
    def __init__(self, row, window, text):
        Label(window, text= text).grid(row=row,columnspan=2)
        self.text = Text(window, height=8,width = 80)

        scroll = Scrollbar(window, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.grid(row=row+1, column=0,columnspan=25, sticky="nsew")
        scroll.grid(row=row+1, column=25, sticky="ns")

        self.text.config(state=DISABLED)