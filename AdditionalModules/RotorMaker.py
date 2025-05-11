import random

n_list=list(range(0,26))
random.shuffle(n_list)
zipped = dict(zip(list(range(0,26)),n_list))
print(zipped)