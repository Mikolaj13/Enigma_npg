from tkinter import *

class IsItEncodingOrDecodingWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Rotor Settings")
        self.is_it_encoding_or_decoding = True
        Button(text="Encoding",width=12,height=2,command=lambda : self.Encoding()).grid(column=0, row=0)
        Button(text="Decoding", width=12, height=2,command=lambda : self.Decoding()).grid(column=1, row=0)
    def Encoding(self):
        self.is_it_encoding_or_decoding = True
        self.destroy()
    def Decoding(self):
        self.is_it_encoding_or_decoding = True
        self.destroy()
