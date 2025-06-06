from tkinter import *
from string import ascii_uppercase

buttons = []
selected_buttons = []
class PlugBoardWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Plug Board")
        ico_path = os.path.join("..", "images", "favicon.ico")
        self.iconbitmap(ico_path)

    # Przyciski do liter
        for index, letter in enumerate(ascii_uppercase):
            buttons.append(PlugBoardButtonMaker(self,index,  letter))

    # Przycisk RESET
        self.reset_btn = Button(self,height = 2, width=8, text="Reset", command=lambda: self.reset_buttons())
        self.reset_btn.grid(row=4, column=10, columnspan=4)

        self.continue_btn = Button(self,text="Continue",height = 2, width=8,command=lambda : self.continue_button())

        self.continue_btn.grid(row=4, column=12, columnspan=4)



    def reset_buttons(self):
        for i, btn in enumerate(buttons):
            btn.button.config(text=ascii_uppercase[i], bg="SystemButtonFace")
        selected_buttons.clear()

    def get_plugboard(self):
        values = []
        for i in buttons:
            values.append(i.current_text)
        return dict(zip(ascii_uppercase, values))
    def continue_button(self):
        self.destroy()



class PlugBoardButtonMaker:
    def __init__(self, window,i, text):
        self.index = i
        self.original_text = text
        self.current_text = text

        self.label = Label(window, text=text+" :",height = 2, width=3)
        self.label.grid(row=(i // 13), column=2 * (i % 13), padx=2, pady=2)

        self.button = Button(window, text=text, height = 2,width=4,
                             command=self.on_button_click)
        self.button.grid(row=(i // 13), column=2 * (i % 13) + 1, padx=2, pady=2)

    def on_button_click(self):
        global selected_buttons
        self.button.config(bg="grey")
        selected_buttons.append(self.index)

        if len(selected_buttons) == 2:
            i1, i2 = selected_buttons
            txt1 = buttons[i1].button['text']
            txt2 = buttons[i2].button['text']
            buttons[i1].button.config(text=txt2, bg="SystemButtonFace")
            buttons[i1].current_text = txt2
            buttons[i2].button.config(text=txt1, bg="SystemButtonFace")
            buttons[i2].current_text = txt1
            selected_buttons.clear()


