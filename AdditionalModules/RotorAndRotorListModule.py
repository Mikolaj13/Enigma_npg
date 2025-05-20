class Rotor:
    def __init__(self,rotor_dictionary,setting=0):
        self.rotor_dictionary = rotor_dictionary
        self.setting = setting

    def __getitem__(self, key):
        return self.rotor_dictionary[key]

    def rotation_values(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.setting += 1
        self.setting %= 26
        self.rotor_dictionary=dict(zip(keys, values[1:]+[values[0]]))

    def setting_values(self,s):
        for i in range(0,s):
            self.rotation_values()

    def rotation_keys(self):
        keys = list(self.rotor_dictionary.keys())
        values = list(self.rotor_dictionary.values())
        self.setting += 1
        self.setting %= 26
        self.rotor_dictionary=dict(zip(keys[1:]+[keys[0]], values))

    def setting_keys(self,s):
        for i in range(0,s):
            self.rotation_keys()


class Rotor_Set:
    def __init__(self,rotor_list, index):
        self.rotor_list = rotor_list
        self.index = index

    def __getitem__(self, key):
        for i in self.rotor_list:
            key = i[key]

    def turn_values(self):
        self.rotor_list[self.index%len(self.rotor_list)].rotation_values()

    def turn_keys(self):
        a = {0:2,1:1,2:0}
        self.rotor_list[a[self.index%len(self.rotor_list)]].rotation_keys()

    def encryption(self, character):
        self.turn_values()
        self.index+=1
        return self[character]

    def decryption(self, character):
        self.turn_keys()
        self.index+=1
        return self[character]