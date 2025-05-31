from tkinter import *
from string import ascii_uppercase



buttons = []
selected_buttons = []
class PlugBoardWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Plug Board")

    # Przyciski do liter
        for index, letter in enumerate(ascii_uppercase):
            buttons.append(PlugBoardButtonMaker(index, self, letter))

    # Przycisk RESET
        self.reset_btn = Button(self, text="Reset", command=self.reset_buttons)
        self.reset_btn.grid(row=4, column=10, columnspan=4)

        self.continue_btn = Button(self,text="Continue")
    #jeszcze nie ma funkcjonalności przycisku
        self.continue_btn.grid(row=4, column=12, columnspan=4)



    def reset_buttons(self):
        for i, btn in enumerate(buttons):
            btn.button.config(text=ascii_uppercase[i], bg="SystemButtonFace")
        selected_buttons.clear()


class PlugBoardButtonMaker:
    def __init__(self, i, window, text):
        self.index = i
        self.original_text = text

        self.label = Label(window, text=text+" :", width=3)
        self.label.grid(row=(i // 13), column=2 * (i % 13), padx=2, pady=2)

        self.button = Button(window, text=text, width=4,
                             command=self.on_button_click)
        self.button.grid(row=(i // 13), column=2 * (i % 13) + 1, padx=2, pady=2)

    def on_button_click(self):
        global selected_buttons
        self.button.config(bg="lightblue")
        selected_buttons.append(self.index)

        if len(selected_buttons) == 2:
            i1, i2 = selected_buttons
            txt1 = buttons[i1].button['text']
            txt2 = buttons[i2].button['text']
            buttons[i1].button.config(text=txt2, bg="SystemButtonFace")
            buttons[i2].button.config(text=txt1, bg="SystemButtonFace")
            selected_buttons.clear()

if _name_ == "_main_":
    app = PlugBoardWindow()
    app.mainloop()
