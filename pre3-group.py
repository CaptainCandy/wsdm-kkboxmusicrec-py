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
#%%


def get_digit(df, col)
    return 10 ** (int(np.log10(df[col].max() + 1)) + 1)


feature_digit = {}
grouping_colns = []
for coln in grouping_colns:
    feature_digit[coln] = get_digit(concat, coln)

#%%


def combine_colname(name1, name2):
    return name1 + '_' + name2


def combine_feature(df, cols1, cols2):
    for col1 in cols1:
        for col2 in cols2:
            df[combine_colname(col1, col2)
               ] = feature_digit[col1] * df[col1] + df[col2]
    return


np.log
