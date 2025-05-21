class Rotor:
    def __init__(self,rotor_dictionary,setting=0):
        self.rotor_dictionary = rotor_dictionary
        self.setting = setting

    def __getitem__(self, key):
        return self.rotor_dictionary[key]

    def rotation(self):
        pass

    def setting(self,s):
        pass


class Encrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.setting += 1
        self.setting %= 26
        self.rotor_dictionary=dict(zip(keys, values[1:]+[values[0]]))
    def setting(self,s):
        for i in range(0,s):
            self.rotation()

class Decrypting_Rotor(Rotor):
    def rotation(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.setting += 1
        self.setting %= 26
        self.rotor_dictionary = dict(zip(keys[1:] + [keys[0]], values))
    def setting(self,s):
        for i in range(0, s):
            self.rotation()

class Rotor_Set:
    def __init__(self, rotor_list, setting=0):
        self.rotor_list = rotor_list
        self.setting = setting

    def __getitem__(self, key):
        for i in self.rotor_list:
            key = i[key]

    def turn(self):
        pass

class Encrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        self.rotor_list[self.setting%len(self.rotor_list)].rotation_values()
        self.setting+=1

class Decrypting_Rotor_Set(Rotor_Set):
    def turn(self):
        a = {0:2,1:1,2:0}
        self.rotor_list[a[self.setting%len(self.rotor_list)]].rotation_keys()
        self.setting+=1

class Enigma_Engine:
    def __init__(self,rotor_dict_list):
        self.e_rotor_set = Encrypting_Rotor_Set([Encrypting_Rotor(i) for i in rotor_dict_list])
        self.d_rotor_set = Decrypting_Rotor_Set([Decrypting_Rotor(dict(zip(i.values,i.keys))) for i in reversed(rotor_dict_list)])

    def encryption(self, character):
        pass
