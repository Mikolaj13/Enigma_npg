class Rotor:
    def __init__(self,rotor_dictionary,setting=0):
        self.rotor_dictionary = rotor_dictionary
        self.setting = setting
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