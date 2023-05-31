#C get_dummies

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
pd.get_dummies(data)

#Без get_dummies

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
unique = data['whoAmI'].unique()
one_hot = pd.DataFrame(0, index=data.index, columns=unique)

for index, row in data.iterrows():
    value = row['whoAmI']
    one_hot.loc[index, value] = 1

one_hot.head()
