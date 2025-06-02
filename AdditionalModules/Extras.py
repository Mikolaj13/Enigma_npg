import string

dictionary = dict(zip(string.ascii_uppercase,list(range(0,26))))
rev_dictionary = dict(zip(list(range(0,26)),string.ascii_uppercase))
SIGN_LIST = [',','.',' ','?','\'','\"',';',':','!','$','\n','1','2','3','4','5','6','7','8','9','-','_','+','=','%','@','#','^','*','(',')','']
ORIGINAL_LETTERS = list(string.ascii_uppercase)
rotor_1= {'A': 'R', 'B': 'F', 'C': 'K', 'D': 'A', 'E': 'U', 'F': 'W', 'G': 'H', 'H': 'J', 'I': 'Q', 'J': 'Z', 'K': 'E', 'L': 'Y', 'M': 'G', 'N': 'P', 'O': 'T', 'P': 'X', 'Q': 'D', 'R': 'M', 'S': 'S', 'T': 'N', 'U': 'I', 'V': 'B', 'W': 'C', 'X': 'V', 'Y': 'L', 'Z': 'O'}

rotor_2= {'A': 'F', 'B': 'G', 'C': 'Y', 'D': 'T', 'E': 'A', 'F': 'H', 'G': 'B', 'H': 'O', 'I': 'V', 'J': 'C', 'K': 'X', 'L': 'D', 'M': 'S', 'N': 'L', 'O': 'E', 'P': 'K', 'Q': 'U', 'R': 'N', 'S': 'R', 'T': 'M', 'U': 'W', 'V': 'Z', 'W': 'P', 'X': 'I', 'Y': 'Q', 'Z': 'J'}

rotor_3= {'A': 'D', 'B': 'S', 'C': 'R', 'D': 'X', 'E': 'P', 'F': 'I', 'G': 'T', 'H': 'M', 'I': 'C', 'J': 'F', 'K': 'Y', 'L': 'Q', 'M': 'J', 'N': 'U', 'O': 'W', 'P': 'B', 'Q': 'H', 'R': 'K', 'S': 'O', 'T': 'A', 'U': 'E', 'V': 'L', 'W': 'V', 'X': 'G', 'Y': 'N', 'Z': 'Z'}
rotor_list = [rotor_1,rotor_2,rotor_3]

opis = ("Aplikacja Enigma umożliwia szyfrowanie tekstu \n "
        "poprzez wpisywanie liter z klawiatury \n"
        " – każda litera jest od razu przekształcana \n "
        " na szyfr. Klawisz Backspace usuwa ostatnio \n"
        " wpisaną literę.Za pomocą przycisku Load  \n "
        "można wczytać plik z tekstem do odszyfrowania.\n"
        " Gotowy szyfr można zapisać klikając Save and Close.")
