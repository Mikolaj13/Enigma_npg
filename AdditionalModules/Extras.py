import string

dictionary = dict(zip(string.ascii_uppercase,list(range(0,26))))
rev_dictionary = dict(zip(list(range(0,26)),string.ascii_uppercase))
SIGN_LIST = [',','.',' ','?','\'','\"',';',':','!','$','\n','1','2','3','4','5','6','7','8','9','-','_','+','=','%','@','#','^','*','(',')','']
ORIGINAL_LETTERS = [
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
    'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
    'Z', 'X', 'C', 'V', 'B', 'N', 'M'
]
rotor_1= {'A': 'R', 'B': 'F', 'C': 'K', 'D': 'A', 'E': 'U', 'F': 'W', 'G': 'H', 'H': 'J', 'I': 'Q', 'J': 'Z', 'K': 'E', 'L': 'Y', 'M': 'G', 'N': 'P', 'O': 'T', 'P': 'X', 'Q': 'D', 'R': 'M', 'S': 'S', 'T': 'N', 'U': 'I', 'V': 'B', 'W': 'C', 'X': 'V', 'Y': 'L', 'Z': 'O'}

rotor_2= {'A': 'F', 'B': 'G', 'C': 'Y', 'D': 'T', 'E': 'A', 'F': 'H', 'G': 'B', 'H': 'O', 'I': 'V', 'J': 'C', 'K': 'X', 'L': 'D', 'M': 'S', 'N': 'L', 'O': 'E', 'P': 'K', 'Q': 'U', 'R': 'N', 'S': 'R', 'T': 'M', 'U': 'W', 'V': 'Z', 'W': 'P', 'X': 'I', 'Y': 'Q', 'Z': 'J'}

rotor_3= {'A': 'D', 'B': 'S', 'C': 'R', 'D': 'X', 'E': 'P', 'F': 'I', 'G': 'T', 'H': 'M', 'I': 'C', 'J': 'F', 'K': 'Y', 'L': 'Q', 'M': 'J', 'N': 'U', 'O': 'W', 'P': 'B', 'Q': 'H', 'R': 'K', 'S': 'O', 'T': 'A', 'U': 'E', 'V': 'L', 'W': 'V', 'X': 'G', 'Y': 'N', 'Z': 'Z'}

rotor_4= {'A': 'I', 'B': 'L', 'C': 'X', 'D': 'V', 'E': 'M', 'F': 'R', 'G': 'J', 'H': 'H', 'I': 'E', 'J': 'W', 'K': 'C', 'L': 'U', 'M': 'Z', 'N': 'A', 'O': 'P', 'P': 'S', 'Q': 'Q', 'R': 'G', 'S': 'K', 'T': 'F', 'U': 'B', 'V': 'T', 'W': 'Y', 'X': 'O', 'Y': 'N', 'Z': 'D'}

rotor_5= {'A': 'C', 'B': 'N', 'C': 'V', 'D': 'R', 'E': 'K', 'F': 'B', 'G': 'W', 'H': 'L', 'I': 'P', 'J': 'Q', 'K': 'H', 'L': 'J', 'M': 'A', 'N': 'S', 'O': 'I', 'P': 'O', 'Q': 'U', 'R': 'E', 'S': 'G', 'T': 'F', 'U': 'X', 'V': 'T', 'W': 'Y', 'X': 'Z', 'Y': 'M', 'Z': 'D'}

rotor_list = [rotor_1,rotor_2,rotor_3,rotor_4,rotor_5]

opis = ("Maszyna szyfrująca Enigma była elektromechanicznym \n"
        "urządzeniem używanym do szyfrowania i deszyfrowania\n"
        " wiadomości, głównie przez Niemców w czasie \n"
        "II wojny światowej. Działała na zasadzie zestawu \n"
        "rotorów, które przy każdym naciśnięciu klawisza \n"
        "zmieniały swoje położenie, tworząc skomplikowany. \n"
        "Każda litera była szyfrowana w inny sposób zależnie\n"
        " od pozycji rotorów, co czyniło kod trudnym do \n"
        "złamania bez znajomości ustawień. Dodatkową warstwę\n"
        " bezpieczeństwa zapewniała tzw. tablica podstawień \n"
        "(plug board), która wymieniała litery parami przed \n"
        "i po przejściu przez rotory.")
