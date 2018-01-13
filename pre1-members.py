#%%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import time
#%%
path = 'F:\\DataMining\\musicRec\\'
members = pd.read_csv(path + 'members.csv')
#%%
columns = ['city', 'gender', 'registered_via']
for column in columns:
    members[column].fillna('na', inplace=True)
    column_encoder = LabelEncoder()
    column_encoder.fit(members[column])
    members[column] = column_encoder.transform(members[column])
'''
columns = ['registration_init_time', 'expiration_date']
for col in columns:
    members[col].fillna('19900101')
'''
#%%
members.values[16867]  # Only this expiration date is out range of mktime.
members.loc[16867, 'expiration_date'] = 20300101
#%%
'''
count = 0
try:
    for i in range(len(members)):
        x = members['registration_init_time'].values[i]
        a = time.mktime(time.strptime(str(x), '%Y%m%d'))
        y = members['expiration_date'].values[i]
        b = time.mktime(time.strptime(str(y), '%Y%m%d'))
        count += 1
except:
    print("Next")
    print(a)
    print(str(b))
    print(x)
    print(y)
    print(i)
print(count)
'''
#%%
members['registration_init_time'] = members['registration_init_time'].apply(lambda x:
                                                                            time.mktime(time.strptime(str(x), '%Y%m%d')))
members['expiration_date'] = members['expiration_date'].apply(lambda x:
                                                              time.mktime(time.strptime(str(x), '%Y%m%d')))
#%%
for col in ['registration_init_time', 'expiration_date']:
    members[col] = np.log1p(members[col])
    #members[col] = members[col].apply(lambda x: np.log1p(x))
members.tail()
#%%


def check_age(x):
    if x < 0:
        return 0
    elif x > 80:
        return 0
    else:
        return x


members['bd'] = members['bd'].apply(check_age)
#%%
members.to_csv(path + 'members_encode.csv', index=False)
print('member done')
