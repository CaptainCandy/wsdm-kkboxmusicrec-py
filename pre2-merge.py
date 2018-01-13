#%%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#%%
path = 'F:\\DataMining\\musicRec\\'


def skiprule(x): return x > 1000


skiprule = None
coltype = {'genre_1st': np.int16, 'language': np.int16, 'artist_feat': np.int16, 'isrc_year': np.float32,
           'genre_2nd': np.int16, 'genre_3rd': np.int16, 'genre_count': np.int16}
# skiprule = None

train = pd.read_csv(path + 'train.csv', skiprows=skiprule)
test = pd.read_csv(path + 'test.csv', skiprows=skiprule)
songs = pd.read_csv(path + 'songs+extra_pro.csv', dtype=coltype)
members = pd.read_csv(path + 'members_encode.csv')

print('loaded')
#%%

# preprocess msno
msno_encoder = LabelEncoder()
msno_encoder.fit(members['msno'].values)
members['msno'] = msno_encoder.transform(members['msno'])
train['msno'] = msno_encoder.transform(train['msno'])
test['msno'] = msno_encoder.transform(test['msno'])

print('MSNO done.')
#%%

# preprocess song_id
song_id_set = set(train['song_id'].append(test['song_id']))

songs['appeared'] = songs['song_id'].apply(
    lambda x: True if x in song_id_set else False)
songs = songs[songs.appeared]
songs.drop('appeared', axis=1, inplace=True)

song_id_encoder = LabelEncoder()
song_id_encoder.fit(train['song_id'].append(test['song_id']))
songs['song_id'] = song_id_encoder.transform(songs['song_id'])
train['song_id'] = song_id_encoder.transform(train['song_id'])
test['song_id'] = song_id_encoder.transform(test['song_id'])

print('Song_id done.')
#%%
# preprocess the features in train.csv & test.csv
columns = ['source_system_tab', 'source_screen_name', 'source_type']
for column in columns:
    train[column].fillna('', inplace=True)
    test[column].fillna('', inplace=True)
    column_encoder = LabelEncoder()
    column_encoder.fit(train[column].append(test[column]))
    train[column] = column_encoder.transform(train[column])
    test[column] = column_encoder.transform(test[column])

print('Source information done.')
#%%

# merge
train = train.merge(songs, on='song_id')
train = train.merge(members, on='msno')
test = test.merge(songs, on='song_id')
test = test.merge(members, on='msno')
print('merge done')
#%%

# time stamp
time_stamp = np.empty((len(train) + len(test)), dtype=int)
time_stamp[:] = range((len(train) + len(test))
train["time_stamp"]=time_stamp[:len(train)]
test['time_stamp']=time_stamp[len(train):len(train) + len(test)]
#%%
train.to_csv(path + 'train_all.csv', index=False)
test.to_csv(path + 'test_all.csv', index=False)
print('concat out')
'''
#%%
train.info()
#%%
test.info()
#%%
songs.info()
'''
