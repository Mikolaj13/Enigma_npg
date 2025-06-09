# Message
import tkinter as tk


root = tk.Tk()

message = tk.Label(root, text="Enigma ")
message.pack()

root.mainloop()





# Creating a button with specified options
import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()

button = tk.Button(root, 
                   text="Enter", 
                   command=button_clicked,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=15,
                   wraplength=100)






button.pack(padx=20, pady=20)

root.mainloop(


#Zarys kalsy setting
class SettingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Enigma Rotor Settings")
        self.geometry("400x400")
        self.config(bg="lightgray")

        self.min_rotors = 2
        self.max_rotors = 5
        self.rotor_count = 3
        self.rotor_positions = [0] * self.rotor_count

        self.create_widgets()

    def create_widgets(self):
        # Nagłówek
        header = tk.Label(self, text="Enigma", font=("Arial", 18, "bold"), bg="lightgray")
        header.pack(pady=10)

        # Sekcja: liczba rotorów
        count_frame = tk.Frame(self, bg="lightgray")
        count_frame.pack(pady=10)

        tk.Label(count_frame, text="Number of rotors:", font=("Arial", 12), bg="lightgray").pack(side=tk.LEFT)

        tk.Button(count_frame, text="-", command=self.decrease_rotor_count, width=3).pack(side=tk.LEFT, padx=5)
        self.count_label = tk.Label(count_frame, text=str(self.rotor_count), font=("Arial", 12), width=2, bg="white")
        self.count_label.pack(side=tk.LEFT)
        tk.Button(count_frame, text="+", command=self.increase_rotor_count, width=3).pack(side=tk.LEFT, padx=5)

        # Sekcja: ustawianie rotorów
        self.rotor_frame = tk.Frame(self, bg="lightgray")
        self.rotor_frame.pack(pady=10)
        self.rotor_controls = []
        self.update_rotor_controls()

        # Przycisk Continue
        continue_btn = tk.Button(self, 
                                 text="Continue", 
                                 command=self.continue_pressed,
                                 bg="lightblue",
                                 font=("Arial", 12, "bold"),
                                 width=20)
        continue_btn.pack(pady=20)
