from tkinter import *
from AdditionalModules.RotorAndRotorListModule import Enigma_Engine
from AdditionalModules.Extras import rotor_list
from AdditionalModules import Widgets_Module_for_mainAppFile as Widgets
import string
class EnigmaApp(Tk):
    def __init__(self,setting_list):
        super().__init__()  # Inicjalizacja klasy bazowej (tk.Tk)

        self.enigma_engine = Enigma_Engine(rotor_list).setting(setting_list)

        self.title("Enigma")
        self.geometry("300x200")

        self.entry_input = Widgets.TextMaker(2, self, "Input")
        self.entry_output = Widgets.TextMaker(4, self, "Output")

    def on_click(self):
        self.label.config(text="Kliknięto przycisk!")

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = EnigmaApp([0,0,0])
    app.mainloop()
