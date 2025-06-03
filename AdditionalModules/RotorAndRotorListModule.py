class Rotor:
    def __init__(self,rotor_dictionary):
        self.rotor_dictionary = rotor_dictionary
        self.rotor_dictionary_copy = rotor_dictionary.copy()
        #na wypadek jakbyśmy chcieli zrobić funkcję resetu

    def __getitem__(self, key):
        return self.rotor_dictionary[key]
    # __getitem__ nadpisuje operator [] klasy
    def rotation(self):
        pass
    # wirtualna metoda do rotacji rotora
    def backspace(self):
        pass

    def setting(self,s):
        pass
    #wirtualna metoda do ustawiania rotora

class Encrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.rotor_dictionary=dict(zip(keys, values[1:]+[values[0]]))
    #nadpisanie metody wirtualnej w klasie dziedziczącej( rozkładamy słownik na klucze i wartości, przerzucamy pierwszą wartość na koniec i składamy z powrotem)
    def backspace(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.rotor_dictionary = dict(zip(keys, [values[-1]] + values[:-1]))

    def setting(self,setting):
        for i in range(0,setting):
            self.rotation()
    #nadpisanie metody wirtualnej w klasie dziedziczącej

class Decrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.rotor_dictionary = dict(zip(keys[1:] + [keys[0]], values))
    def backspace(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.rotor_dictionary = dict(zip( [keys[-1]] + keys[:-1],values))
    # nadpisanie metody wirtualnej w klasie dziedziczącej( rozkładamy słownik na klucze i wartości, przerzucamy ostatni klucz na początek i składamy z powrotem)
    def setting(self,setting):
        for i in range(0, setting):
            self.rotation()
    # nadpisanie metody wirtualnej w klasie dziedziczącej

class Rotor_Set:
    def __init__(self, rotor_list, index=0):
        self.rotor_list = rotor_list
        self.index = index
        self.dictionary_for_decryption = dict(zip(range(0, len(self.rotor_list)), reversed(range(0, len(self.rotor_list)))))
    #index to generalnie jest to, na której literze z kolei jesteśmy
    def __getitem__(self, key):
        for i in self.rotor_list:
            key = i[key]
        return key
    # __getitem__ nadpisuje operator [] klasy
    def turn(self):
        pass
    def backspace(self):
        pass
    # wirtualna metoda do pełnej tury całego zestawu
    def setting(self,setting_list):
        pass
    # wirtualna metoda do ustawiania całego zestawu

class Encrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        self.rotor_list[self.index % len(self.rotor_list)].rotation()
        self.index+=1
    # nadpisanie metody wirtualnej w klasie dziedziczącej(obracamy tylko ten rotor, który jest na pozycji reszty z dzielenia indexu przez ilość rotorów w zestawie)

    def backspace(self):
        self.index -= 1
        self.rotor_list[self.index % len(self.rotor_list)].backspace()

    def setting(self,setting_list):
        for i,j in enumerate(setting_list):
            self.rotor_list[i].setting(j)
    # wirtualna metoda do ustawiania całego zestawu
class Decrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        self.rotor_list[self.dictionary_for_decryption[self.index % len(self.rotor_list)]].rotation()
        self.index+=1
    # nadpisanie metody wirtualnej w klasie dziedziczącej(obracamy tylko ten rotor, który jest na pozycji reszty z dzielenia indexu przez ilość rotorów w zestawie)

    def backspace(self):

        self.index -= 1
        self.rotor_list[self.dictionary_for_decryption[self.index % len(self.rotor_list)]].backspace()

    def setting(self,setting_list):
        for i,j in enumerate(reversed(setting_list)):
            self.rotor_list[i].setting(j)
    # wirtualna metoda do ustawiania całego zestawu


class Enigma_Engine:
    def __init__(self,rotor_dict_list,plug_board):
        self.e_rotor_set = Encrypting_Rotor_Set([Encrypting_Rotor(i) for i in rotor_dict_list])
        self.d_rotor_set = Decrypting_Rotor_Set([Decrypting_Rotor(dict(zip(i.values(),i.keys()))) for i in reversed(rotor_dict_list)])
        self.plug_board = plug_board
        self.reversed_plug_board = dict(zip(plug_board.values(),plug_board.keys()))
    def encryption(self, character):
        self.e_rotor_set.turn()
        self.d_rotor_set.turn()
        return self.plug_board[self.e_rotor_set[character]]
        
    def decryption(self, character):
        self.d_rotor_set.turn()
        self.e_rotor_set.turn()
        return self.reversed_plug_board[self.d_rotor_set[character]]
    def backspace(self):
        self.e_rotor_set.backspace()
        self.d_rotor_set.backspace()
    def setting(self, setting_list):
        self.e_rotor_set.setting(setting_list)
        self.d_rotor_set.setting(setting_list)


