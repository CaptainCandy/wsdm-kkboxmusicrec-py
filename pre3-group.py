#%%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#%%


def skiprule(x): return x > 10000


path = 'F:\\DataMining\\musicRec\\'
coltype = {'genre_1st': np.int16, 'language': np.int16, 'artist_feat': np.int16, 'isrc_year': np.float32,
           'genre_2nd': np.int16, 'genre_3rd': np.int16, 'genre_count': np.int16}
#skiprule = None

train = pd.read_csv(path + 'train_all.csv', skiprows=skiprule)
test = pd.read_csv(path + 'test_all.csv', skiprows=skiprule)

print('loaded')
#%%

# Define function and colnames list.
grouping_colns = ['msno']
gruop_key_colns = []


def get_digit(ser)
    return 10 ** (int(np.log10(ser.max() + 1)) + 1)


def combine_colname(name1, name2):
    return name1 + '_' + name2


def pair_feature(df, cols1, cols2):
    '''
    return a series pair the two IDs.
    '''
    series = feature_digit[col1] * df[col1] + df[col2]
    return series


def get_group_mean(dftr, dfva, pair_tr):
    map_mean = dftr.groupby(pair_tr).target.mean()

    pair_coln = combine_colname(coln1, coln2)

    for col1 in list1:
        for col2 in list2:
            group_tr = pair_feature(dftr, col1, col2)
            map_mean = dftr.groupby(group_tr).target.mean()

    combine_feature(dftr, list1, list2)
    combine_feature(dfva, list1, list2)
    map_mean = dftr[]


#%%
feature_digit = {}
for coln in grouping_colns:
    feature_digit[coln] = get_digit(train[coln].append(test[coln]))
#%%
train.info()
