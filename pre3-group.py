#%%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#%%


def skiprule(x): return x > 10000


path = 'F:\\DataMining\\musicRec\\'
coltype = {'genre_1st': np.int16, 'language': np.int16, 'artist_feat': np.int16, 'isrc_year': np.float32,
           'genre_2nd': np.int16, 'genre_3rd': np.int16, 'genre_count': np.int16}
skiprule = None

train = pd.read_csv(path + 'train_all.csv', skiprows=skiprule)
test = pd.read_csv(path + 'test_all.csv', skiprows=skiprule)

print('loaded')
