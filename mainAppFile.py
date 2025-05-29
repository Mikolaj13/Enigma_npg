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

        self.input_text_field = Widgets.TextMaker(2, self, "Input")
        self.output_text_field = Widgets.TextMaker(4, self, "Output")

        self.list_of_output_buttons = list()
        self.list_of_input_buttons = list()

        for i, l in enumerate(string.ascii_uppercase):
            row = 6
            col = i
            self.list_of_input_buttons.append(Widgets.ButtonIOMaker(row, col, l, self))
            self.list_of_output_buttons.append(Widgets.ButtonIOMaker(row + 3, col, l, self))

    def on_key_press(self,event):

        character = event.char.upper()
        print(character)

        if event.keysym == "BackSpace" and  len(self.input_text_field.text.get("1.0", "end-1c")) >0:
            text = self.input_text_field.text.get("1.0", "end-1c")

            self.input_text_field.backspace()
            self.output_text_field.backspace()

            if text[-1] in string.ascii_uppercase:
                self.enigma_engine.backspace()

        if character in SIGN_LIST:
            self.input_text_field.typing(character)

            self.output_text_field.typing(character)

        if character in string.ascii_uppercase:

            if is_it_encryption_or_decryption:
                character_after = self.enigma_engine.encryption(character)
            else:
                character_after = self.enigma_engine.decryption(character)

            self.input_text_field.typing(character)

            self.output_text_field.typing(character_after)

            self.list_of_input_buttons[string.ascii_uppercase.index(character)].clicked()

            self.list_of_output_buttons[string.ascii_uppercase.index(character_after)].clicked()


# Uruchomienie aplikacji
if __name__ == "__main__":
    app = EnigmaApp([0,0,0])
    app.bind("<KeyPress>", app.on_key_press)
    app.mainloop()
