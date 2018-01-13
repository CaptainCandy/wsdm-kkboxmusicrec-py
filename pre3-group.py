#%%
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#%%


def skiprule(x): return x >10000


path = 'F:\\DataMining\\musicRec\\'
coltype = {'genre_1st': np.int16, 'language': np.int16, 'artist_feat': np.int16, 'isrc_year': float,
           'genre_2nd': np.int16, 'genre_3rd': np.int16, 'genre_count': np.int16}
#skiprule = None

train = pd.read_csv(path + 'train_all.csv', skiprows=skiprule)
test = pd.read_csv(path + 'test_all.csv', skiprows=skiprule)

print('loaded')
#%%

# Define function and colnames list.


def create_pair_cols(tr, te, cols1, cols2):
    pair_cols = []
    for col1 in cols1:
        for col2 in cols2:
            new_col = combine_colname(col1, col2)
            pair_cols.append(new_col)
            tr[new_col] = pair_feature(tr, col1, col2)
            te[new_col] = pair_feature(te, col1, col2)
    return pair_cols


def create_statistical_features(tr, te, pair_cols):
    statis_cols = []
    for col in pair_cols:
        statis_cols.append(add_aggregate_count(tr, te, col))
        statis_cols.append(add_aggregate_mean(tr, te, col))
    return statis_cols


def create_chorological_features(tr, te, pair_cols):
    choro_cols = []
    tr_n_te = pd.concat([tr, te])
    for col in pair_cols:
        choro_cols.append(add_time_previous(tr_n_te, col, 'time'))
        choro_cols.append(add_time_next(tr_n_te, col, 'time'))
    for col in choro_cols:
        tr[col] = tr_n_te[col].values[:len(tr)]
        te[col] = tr_n_te[col].values[len(tr):len(tr) + len(te)]
    return choro_cols


def get_digit(ser):
    return 10 ** (int(np.log10(ser.max() + 1)) + 1)


def combine_colname(name1, name2):
    return name1 + '_' + name2


def pair_feature(df, col1, col2):
    '''
    return a series pair the two IDs.
    '''
    series = feature_digit[col2] * df[col1] + df[col2]
    return series


def add_aggregate_mean(dftr, dfva, agg_col):
    map_mean = dftr.groupby(agg_col).target.mean()
    colname = combine_colname('mean', agg_col)
    dftr[colname] = dftr[agg_col].map(map_mean).fillna(-1)
    dfva[colname] = dfva[agg_col].map(map_mean).fillna(-1)
    return colname


def add_aggregate_count(dftr, dfva, agg_col):
    map_count = dftr.groupby(agg_col).size()
    colname = combine_colname('count', agg_col)
    dftr[colname] = dftr[agg_col].map(map_count).fillna(-1)
    dfva[colname] = dfva[agg_col].map(map_count).fillna(-1)
    return colname


def add_time_previous(concat, agg_col, time_coln):
    time_stamp_col = time_coln
    previou = {}
    new_col = combine_colname('timediff_prev', agg_col)
    nparray = np.zeros(len(concat))
    max_len = len(concat)
    #del nparray
    for i in range(len(concat)):
        if concat[agg_col].values[i] in previou:
            nparray[i] = previou[concat[agg_col].values[i]]
        else:
            nparray[i] = max_len
        previou[concat[agg_col].values[i]] = concat[time_stamp_col].values[i]
    concat[new_col] = nparray
    return new_col


def add_time_next(concat, agg_col, time_coln):
    time_stamp_col = time_coln
    next = {}
    new_col = combine_colname('timediff_next', agg_col)
    nparray = np.zeros(len(concat))
    max_len = len(concat)
    #del nparray
    for i in range(len(concat) - 1, -1, -1):
        if concat[agg_col].values[i] in next:
            nparray[i] = next[concat[agg_col].values[i]]
        else:
            nparray[i] = max_len
        next[concat[agg_col].values[i]] = concat[time_stamp_col].values[i]
    concat[new_col] = nparray
    return new_col


columns1 = ['msno', 'gender', 'registered_via']
columns2 = ['source_system_tab', 'source_screen_name', 'source_type']
columns3 = ['language', 'artist_1st',  'composer_1st',  'lyricist_1st', 'isrc_year',
            'isrc_country', 'isrc_comp', 'genre_1st', 'genre_2nd']
print('definition done')
#%%
feature_digit = {}
all_columns = columns1
all_columns.extend(columns2)
all_columns.extend(columns3)
for coln in all_columns:
    feature_digit[coln] = get_digit(train[coln].append(test[coln]))
pair_cols_list = []
statis_cols_list = []
choro_cols_list = []
feature_digit
#%%
# Add new pairs or triples.
pair_cols_list.append(create_pair_cols(train, test, columns1, columns2))
pair_cols_list.append(create_pair_cols(train, test, columns1, columns3))
print('new pairs done')
#%%
# Add new features.
statis_cols_list.append(create_statistical_features(
    train, test, pair_cols_list[0]))
choro_cols_list.append(create_chorological_features(
    train, test, pair_cols_list[0]))
statis_cols_list.append(create_statistical_features(
    train, test, pair_cols_list[1]))
choro_cols_list.append(create_chorological_features(
    train, test, pair_cols_list[1]))
print('new feats done')
#%%
train.info()
#%%
print(test.columns)
print(train.columns)
#%%
print()
#%%
print(len(train.columns))
#%%

#%%
test.head(10)
#%%
