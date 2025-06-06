from tkinter import *

class IsItEncodingOrDecodingWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Rotor Settings")
        self.is_it_encoding_or_decoding = True
        Button(text="Encoding",width=12,height=2,command=lambda : self.encoding()).grid(column=0, row=0)
        Button(text="Decoding", width=12, height=2,command=lambda : self.decoding()).grid(column=1, row=0)
    def encoding(self):
        self.is_it_encoding_or_decoding = True
        self.destroy()
    def decoding(self):
        self.is_it_encoding_or_decoding = False
        self.destroy()
    def get(self):
        return self.is_it_encoding_or_decoding
