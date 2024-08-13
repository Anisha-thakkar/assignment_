dict_ = {1:'one',2:'two',3:'three',4:'four',5:'five'}

import csv
import pandas as pd
df=pd.read_csv('/home/anisha/Assignment/a1_14_8_24/test2.csv')
l=df.columns.values.tolist()

if l[0]=='GET':
    print(l[1])
else:
    new_dict={l[1]:l[2]}
    dict_.update(new_dict)
    print(dict_)