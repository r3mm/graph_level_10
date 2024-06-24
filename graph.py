import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()
one_hot_data = pd.DataFrame()

for value in unique_values:
    one_hot_data[value] = data['whoAmI'].apply(lambda x: 1 if x == value else 0)

data = pd.concat([data, one_hot_data], axis=1)

print(data.head())
