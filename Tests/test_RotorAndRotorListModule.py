from unittest import TestCase
from AdditionalModules import Extras
from AdditionalModules.RotorAndRotorListModule import Enigma_Engine


class TestEnigma_Engine(TestCase):
    def test_encryption(self):
        enigma_machine = Enigma_Engine(Extras.rotor_list)
        enigma_machine.setting([1,2,3])
        test_text = "AMERICA"
        a = ""
        b = ""
        for i in test_text:
            a+=enigma_machine.encryption(i)
        print(a)
        for i in a:
            b+=enigma_machine.decryption(i)
        print(b)
        if test_text != b:
            self.fail("Test")
# test działania silnika