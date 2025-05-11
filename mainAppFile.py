from tkinter import *

class EnigmaApp(Tk):
    def __init__(self):
        super().__init__()  # Inicjalizacja klasy bazowej (tk.Tk)
        self.title("Enigma")
        self.geometry("300x200")


    def on_click(self):
        self.label.config(text="Kliknięto przycisk!")

# Uruchomienie aplikacji
if __name__ == "__main__":
    app = EnigmaApp()
    app.mainloop()
