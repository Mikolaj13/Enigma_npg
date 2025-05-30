from tkinter import *
from AdditionalModules.RotorAndRotorListModule import Enigma_Engine
from AdditionalModules.Extras import rotor_list
from AdditionalModules.Extras import SIGN_LIST
from AdditionalModules import Widgets_Module_for_mainAppFile as Widgets
import string

is_it_encryption_or_decryption=True
class EnigmaApp(Tk):
    def __init__(self,setting_list):
        super().__init__()  # Inicjalizacja klasy bazowej (tk.Tk)

        self.enigma_engine = Enigma_Engine(rotor_list)
        self.enigma_engine.setting(setting_list)

        self.title("Enigma")

        self.IO_text_fields = Widgets.TextIOPair(10,self)

        Label().grid(row=4, column=0) # wypełnienie między klawiaturami
        self.list_of_output_buttons = list()
        self.list_of_input_buttons = list()

        for i, j in enumerate(string.ascii_uppercase):
            if i < 20:
                self.list_of_output_buttons.append(Widgets.ButtonIOMaker((i//10),i%10,j,self,"white"))
                self.list_of_input_buttons.append(Widgets.ButtonIOMaker((i // 10)+5, i % 10, j, self,"grey"))
            else:
                self.list_of_output_buttons.append(Widgets.ButtonIOMaker((i//10),(i%10)+2,j,self,"white"))
                self.list_of_input_buttons.append(Widgets.ButtonIOMaker((i // 10)+5, (i % 10) + 2, j, self,"grey"))

    def on_key_press(self,event):

        character = event.char.upper()
        if event.keysym == "BackSpace" and  self.IO_text_fields.getlength() >0:
            if self.IO_text_fields.getlastletter() in string.ascii_uppercase:
                self.enigma_engine.backspace()
            self.IO_text_fields.backspace()

        if character in SIGN_LIST:
            self.IO_text_fields.typing(character,character)

        if character in string.ascii_uppercase:

            if is_it_encryption_or_decryption:
                character_after = self.enigma_engine.encryption(character)
            else:
                character_after = self.enigma_engine.decryption(character)

            self.IO_text_fields.typing(character,character_after)

            self.list_of_input_buttons[string.ascii_uppercase.index(character)].clicked()
            self.list_of_output_buttons[string.ascii_uppercase.index(character_after)].clicked()


# Uruchomienie aplikacji
if __name__ == "__main__":
    app = EnigmaApp([0,0,0])
    app.bind("<KeyPress>", app.on_key_press)
    app.mainloop()
