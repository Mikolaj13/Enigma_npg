class Rotor:
    def __init__(self,rotor_dictionary,current_setting=0):
        self.rotor_dictionary = rotor_dictionary
        self.rotor_dictionary_copy = rotor_dictionary.copy()
        #na wypadek jakbyśmy chcieli zrobić funkcję resetu
        self.current_setting = current_setting

    def __getitem__(self, key):
        return self.rotor_dictionary[key]
    # __getitem__ nadpisuje operator [] klasy
    def rotation(self):
        pass

    def setting(self,s):
        pass


class Encrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.current_setting += 1
        self.current_setting %= 26
        self.rotor_dictionary=dict(zip(keys, values[1:]+[values[0]]))
    def setting(self,setting):
        for i in range(0,setting):
            self.rotation()

class Decrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.current_setting += 1
        self.current_setting %= 26
        self.rotor_dictionary = dict(zip(keys[1:] + [keys[0]], values))
    def setting(self,setting):
        for i in range(0, setting):
            self.rotation()
#klasa rotor i klasy dziedziczące działają


class Rotor_Set:
    def __init__(self, rotor_list, index=0):
        self.rotor_list = rotor_list
        self.index = index

    def __getitem__(self, key):
        for i in self.rotor_list:
            key = i[key]
        return key

    def turn(self):
        pass

    #dodana funkcjonalność mam na dzieję że o to chodzi 
    def setting(self,settings_list):
        for rotor, setting in zip(self.rotor_list, settings_list):
            rotor.setting(setting)
        pass

class Encrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        self.rotor_list[self.index % len(self.rotor_list)].rotation()
        self.index+=1

class Decrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        a = {0:2,1:1,2:0}
        self.rotor_list[a[self.index % len(self.rotor_list)]].rotation()
        self.index+=1

class Enigma_Engine:
    def __init__(self,rotor_dict_list):
        self.e_rotor_set = Encrypting_Rotor_Set([Encrypting_Rotor(i) for i in rotor_dict_list])
        self.d_rotor_set = Decrypting_Rotor_Set([Decrypting_Rotor(dict(zip(i.values(),i.keys()))) for i in reversed(rotor_dict_list)])

    def encryption(self, character):
        self.e_rotor_set.turn()
        return self.e_rotor_set[character]
        
    def decryption(self, character):
        self.d_rotor_set.turn()
        return self.d_rotor_set[character]

    def setting(self, settings_list):
        self.e_rotor_set.setting(settings_list)
        self.d_rotor_set.setting(settings_list[::-1])


