from tkinter import *

class ButtonIOMaker:
    def __init__(self, row, col, text, window,colour):
        self.window = window
        self.colour = colour
        self.button = Button(window,width=4, height=2 , text=text, bg="light grey")
        self.button.grid(row=row, column=col)
        self.button.config(state=DISABLED)

    def clicked(self):
        self.button.config(bg=self.colour)
        self.window.after(200, lambda: self.button.config(bg="light grey"))

class TextMaker:
    def __init__(self, row,col, window, text):
        Label(window, text= text).grid(row=row,column = col)
        self.text = Text(window, height=8,width = 40)

        scroll = Scrollbar(window, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)

        self.text.grid(row=row+1, column=col,columnspan=12, sticky="nsew")
        scroll.grid(row=row+1, column=col+13, sticky="ns")

        self.text.config(state=DISABLED)

    def typing(self,char):
        self.text.config(state = NORMAL)
        self.text.insert(END,char)
        self.text.config(state= DISABLED)

    def backspace(self):
        self.text.config(state=NORMAL)
        self.text.delete("end-2c", "end-1c")
        self.text.config(state=DISABLED)

    def getlength(self):
        return len(self.text.get("1.0", "end-1c"))
    def getlastletter(self):
        return self.text.get("1.0", "end-1c")[-1]


class TextIOPair:
    def __init__(self, row, window):
        self.input_text_field = TextMaker(row, 0, window, "Input")
        self.output_text_field = TextMaker(row, 14, window, "Output")
    def typing(self,character_in,character_out):
        self.input_text_field.typing(character_in)
        self.output_text_field.typing(character_out)
    def backspace(self):
        self.input_text_field.backspace()
        self.output_text_field.backspace()
    def getlength(self):
        return self.input_text_field.getlength()
    def getlastletter(self):
        return self.input_text_field.getlastletter()