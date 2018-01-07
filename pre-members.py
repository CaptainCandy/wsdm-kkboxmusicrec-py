#%%
import pandas as pd
import numpy as py
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

members['registration_init_time'] = members['registration_init_time'].apply(
    lambda x: time.mktime(time.strptime(str(x), '%Y%m%d')))
members['expiration_date'] = members['expiration_date'].apply(
    lambda x: time.mktime(time.strptime(str(x), '%Y%m%d')))
#%%
members.to_csv(path + 'members_encode.csv', index=False)
