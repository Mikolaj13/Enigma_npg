from tkinter import *
from tkinter import filedialog
from AdditionalModules.RotorAndRotorListModule import Enigma_Engine
from AdditionalModules import Extras
from AdditionalModules import Widgets_Module_for_MainWindow as Widgets
import string

is_it_encryption_or_decryption=True
class EnigmaApp(Tk):
    def __init__(self,setting_list,plug_board):
        super().__init__()

        self.enigma_engine = Enigma_Engine(Extras.rotor_list[:len(setting_list)],plug_board)
        self.enigma_engine.setting(setting_list)

        self.title("Enigma")
        #pola tekstowe
        self.IO_text_fields = Widgets.TextIOPair(10,self)
        Label().grid(row=4, column=0) # wypełnienie między klawiaturami

        # przyciski funkcyjne
        Button(self,text="Load",width=15,height=2,command=lambda: self.load()).grid(row=0,column=13,columnspan=3)
        Button(self, text="Save and close", width=15, height=2, command=lambda: self.save_and_close()).grid(row=0, column=16, columnspan=3)
        Button(self, text="Close", width=15, height=2, command=lambda: self.destroy()).grid(row=0,column=19,columnspan=3)
        #
        Label(self, text=Extras.opis).grid(row=1, column=13, columnspan=12, rowspan=7)
        #listy "światełek"
        self.list_of_output_buttons = list()
        self.list_of_input_buttons = list()

        #rozmieszczanie światełek
        for i, j in enumerate(Extras.ORIGINAL_LETTERS):
            if i < 20:
                self.list_of_output_buttons.append(Widgets.ButtonIOMaker((i//10),i%10,j,self,"white"))
                self.list_of_input_buttons.append(Widgets.ButtonIOMaker((i // 10)+5, i % 10, j, self,"grey"))
            else:
                self.list_of_output_buttons.append(Widgets.ButtonIOMaker((i//10),(i%10)+2,j,self,"white"))
                self.list_of_input_buttons.append(Widgets.ButtonIOMaker((i // 10)+5, (i % 10) + 2, j, self,"grey"))


    # metoda sczytująca input z klawiatury
    def on_key_press(self,event):

        character = event.char.upper()

        #cofanie
        if event.keysym == "BackSpace" and  self.IO_text_fields.getlength() >0:
            if self.IO_text_fields.getlastletter() in string.ascii_uppercase:
                self.enigma_engine.backspace()
            self.IO_text_fields.backspace()
        #nie wiem po co to jest ale bez tego przy naciśnięciu shifta rotory się obracają niepotrzebnie
        elif event.keysym == "LeftShift":
            pass
        #sprawdzamy czy znak jest na liście znaków interpunkcyjnych, których nie zmieniamy
        elif character in Extras.SIGN_LIST:
            self.IO_text_fields.typing(character,character)

        #sprawdzamy czy znak jest literą
        elif character in string.ascii_uppercase:

            if is_it_encryption_or_decryption:
                character_after = self.enigma_engine.encryption(character)
            else:
                character_after = self.enigma_engine.decryption(character)

            self.IO_text_fields.typing(character,character_after)

            self.list_of_input_buttons[Extras.ORIGINAL_LETTERS.index(character)].clicked()
            self.list_of_output_buttons[Extras.ORIGINAL_LETTERS.index(character_after)].clicked()


    # metoda do ładowania plików
    def load(self):
        filepath = filedialog.askopenfilename(
            title="Wybierz plik tekstowy",
            filetypes=[("Pliki tekstowe", "*.txt")]
        )

        if not filepath:
            print("Nie wybrano pliku.")
            return None

        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                for character in file.read():
                    if character in Extras.SIGN_LIST:
                        self.IO_text_fields.typing(character, character)

                    if character in string.ascii_uppercase:

                        if is_it_encryption_or_decryption:
                            character_after = self.enigma_engine.encryption(character)
                        else:
                            character_after = self.enigma_engine.decryption(character)

                        self.IO_text_fields.typing(character, character_after)

        except Exception as e:
            print(f"Wystąpił błąd podczas odczytu pliku: {e}")
            return None

    #metoda do zapisywania plików
    def save_and_close(self):
        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Pliki tekstowe", "*.txt")],
            title="Zapisz jako"
        )
        if filepath:
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(self.IO_text_fields.output_text_field.text.get("1.0", END))
            print(f"Zapisano do: {filepath}")

        self.destroy()

