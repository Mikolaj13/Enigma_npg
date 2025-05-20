import string
dictionary = dict(zip(string.ascii_uppercase,list(range(0,26))))
rev_dictionary = dict(zip(list(range(0,26)),string.ascii_uppercase))
SIGN_LIST = [',','.',' ','?','\'','\"',';',':','!','$','\n','1','2','3','4','5','6','7','8','9']
ORIGINAL_LETTERS = list(string.ascii_uppercase)
rotor_1= {'A': 'R', 'B': 'F', 'C': 'K', 'D': 'A', 'E': 'U', 'F': 'W', 'G': 'H', 'H': 'J', 'I': 'Q', 'J': 'Z', 'K': 'E', 'L': 'Y', 'M': 'G', 'N': 'P', 'O': 'T', 'P': 'X', 'Q': 'D', 'R': 'M', 'S': 'S', 'T': 'N', 'U': 'I', 'V': 'B', 'W': 'C', 'X': 'V', 'Y': 'L', 'Z': 'O'}
rev_rotor_1= {'R': 'A', 'F': 'B', 'K': 'C', 'A': 'D', 'U': 'E', 'W': 'F', 'H': 'G', 'J': 'H', 'Q': 'I', 'Z': 'J', 'E': 'K', 'Y': 'L', 'G': 'M', 'P': 'N', 'T': 'O', 'X': 'P', 'D': 'Q', 'M': 'R', 'S': 'S', 'N': 'T', 'I': 'U', 'B': 'V', 'C': 'W', 'V': 'X', 'L': 'Y', 'O': 'Z'}
rotor_2= {'A': 'F', 'B': 'G', 'C': 'Y', 'D': 'T', 'E': 'A', 'F': 'H', 'G': 'B', 'H': 'O', 'I': 'V', 'J': 'C', 'K': 'X', 'L': 'D', 'M': 'S', 'N': 'L', 'O': 'E', 'P': 'K', 'Q': 'U', 'R': 'N', 'S': 'R', 'T': 'M', 'U': 'W', 'V': 'Z', 'W': 'P', 'X': 'I', 'Y': 'Q', 'Z': 'J'}
rev_rotor_2= {'F': 'A', 'G': 'B', 'Y': 'C', 'T': 'D', 'A': 'E', 'H': 'F', 'B': 'G', 'O': 'H', 'V': 'I', 'C': 'J', 'X': 'K', 'D': 'L', 'S': 'M', 'L': 'N', 'E': 'O', 'K': 'P', 'U': 'Q', 'N': 'R', 'R': 'S', 'M': 'T', 'W': 'U', 'Z': 'V', 'P': 'W', 'I': 'X', 'Q': 'Y', 'J': 'Z'}
rotor_3= {'A': 'D', 'B': 'S', 'C': 'R', 'D': 'X', 'E': 'P', 'F': 'I', 'G': 'T', 'H': 'M', 'I': 'C', 'J': 'F', 'K': 'Y', 'L': 'Q', 'M': 'J', 'N': 'U', 'O': 'W', 'P': 'B', 'Q': 'H', 'R': 'K', 'S': 'O', 'T': 'A', 'U': 'E', 'V': 'L', 'W': 'V', 'X': 'G', 'Y': 'N', 'Z': 'Z'}
rev_rotor_3= {'D': 'A', 'S': 'B', 'R': 'C', 'X': 'D', 'P': 'E', 'I': 'F', 'T': 'G', 'M': 'H', 'C': 'I', 'F': 'J', 'Y': 'K', 'Q': 'L', 'J': 'M', 'U': 'N', 'W': 'O', 'B': 'P', 'H': 'Q', 'K': 'R', 'O': 'S', 'A': 'T', 'E': 'U', 'L': 'V', 'V': 'W', 'G': 'X', 'N': 'Y', 'Z': 'Z'}
