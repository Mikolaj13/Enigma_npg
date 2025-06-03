import random
import string
n_list=list(string.ascii_uppercase)
random.shuffle(n_list)
zipped = dict(zip(string.ascii_uppercase,n_list))
rev_zipped = dict(zip(n_list,string.ascii_uppercase))
print("rotor_5=",zipped)
print(dict(zip(range(0,3),reversed(range(0,3)))))
