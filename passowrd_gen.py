import numpy as np
import pandas as pd
import string

num = string.digits
lettr_up = string.ascii_uppercase
lettr_low = string.ascii_lowercase
symb = string.punctuation
pass_dict = np.array([num, lettr_up, lettr_low, symb])

password = ''
length = 20
num_count = 0
lettr_up_count = 0
lettr_low_count = 0
symb_count = 0
for i in range(length):
    choice_set = pass_dict[np.random.choice(4, 1)[0]]
    set_len = len(choice_set)
    password += choice_set[np.random.choice(set_len, 1)[0]]
for chart in password:
    if chart in num:
        num_count += 1
    elif chart in lettr_up:
        lettr_up_count += 1
    elif chart in lettr_low:
        lettr_low_count += 1
    else:
        symb_count += 1
num_series = pd.Series([num_count, lettr_up_count, lettr_low_count, symb_count])

while any(num_series == 0):
    num_rank = num_series.rank()
    # select the least frequency list
    min_sel = num_series.index[num_rank == min(num_rank)][0]
    max_sel = num_series.index[num_rank == max(num_rank)][0]
    max_list = []
    for i in range(length):
        if password[i] in pass_dict[max_sel]:
            max_list.append(i)
    rep_posi = np.random.choice(max_list, 1)[0]
    list(password)[rep_posi] = pass_dict[min_sel][np.random.choice(len(pass_dict[min_sel]), 1)[0]]
    password = ''.join(password)
    # check again
    nc = 0
    lu = 0
    ll = 0
    sb = 0
    for chart in password:
        if chart in num:
            nc += 1
        elif chart in lettr_up:
            lu += 1
        elif chart in lettr_low:
            ll += 1
        else:
            sb += 1
    num_series = pd.Series([nc, lu, ll, sb])
    
print(password)