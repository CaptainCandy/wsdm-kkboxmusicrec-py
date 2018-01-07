#%%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#%%
# 读取文件
path = 'F:\\DataMining\\musicRec\\'
songs = pd.read_csv(path + "songs.csv")
#                         ,usecols=['genre_ids'])  # , skiprows=lambda x: x > 60)

#%%
# 处理属性：风格
temp_array = np.zeros((len(songs), 4))
for i in range(len(songs)):
    x = songs['genre_ids'].values[i]
    if not isinstance(x, str):
        continue
    list_id = str(x).split('|')
    temp_array[i, 0] = len(list_id)
    num_id = len(list_id)
    if num_id > 0:
        temp_array[i, 1] = int(list_id[0])
        if num_id > 1:
            temp_array[i, 2] = int(list_id[1])
            if num_id > 2:
                temp_array[i, 3] = int(list_id[2])
songs['genre_count'] = temp_array[:, 0]
songs['genre_1st'] = temp_array[:, 1]
songs['genre_2nd'] = temp_array[:, 2]
songs['genre_3rd'] = temp_array[:, 3]

#%%
genre_encoder = LabelEncoder()
genre_encoder.fit((songs.genre_1st.append(
    songs.genre_2nd)).append(songs.genre_3rd))
songs['genre_1st'] = genre_encoder.transform(songs['genre_1st'])
songs['genre_2nd'] = genre_encoder.transform(songs['genre_2nd'])
songs['genre_3rd'] = genre_encoder.transform(songs['genre_3rd'])
#%%
genre_encoder = LabelEncoder()
songs['genre_ids'] = genre_encoder.fit_transform(songs['genre_ids'])
#songs.drop('genre_ids', axis=1, inplace=True)

#%%


def get_acl_count_name(x, filter):
    '''
    提取歌手、作词、作曲的数量与首席是什么。
    '''
    if not isinstance(x, str):
        return (0, '')
    else:
        dict_count = {}
        for sign in filter:
            dict_count[sign] = x.count(sign)
        for sign in filter:
            if dict_count[sign] > 0:
                x = x.split(sign)[0]
        return (sum(dict_count.values()) + 1, x.strip())


len_songs = len(songs)
temp_array = np.zeros((len_songs, 3))
temp_array_s = np.empty((len_songs, 3), '<U10')
filter1 = ['and', '&', 'feat']
filter2 = ['\\', '|', '/']
for col in ['artist_name', 'composer', 'lyricist']:
    songs[col].fillna('')
for i in range(len_songs):
    (count, name) = get_acl_count_name(
        songs['artist_name'].values[i], filter1)
    temp_array[i, 0] = count
    temp_array_s[i, 0] = name
    (count, name) = get_acl_count_name(
        songs['composer'].values[i], filter2)
    temp_array[i, 1] = count
    temp_array_s[i, 1] = name
    (count, name) = get_acl_count_name(
        songs['lyricist'].values[i], filter2)
    temp_array[i, 2] = count
    temp_array_s[i, 2] = name

for j in range(3):
    encoder = LabelEncoder()
    temp_array_s[:, j] = encoder.fit_transform(temp_array[:, j])

songs['number_artist'] = temp_array[:, 0]
songs['artist_1st'] = temp_array_s[:, 0]
songs['number_composer'] = temp_array[:, 1]
songs['composer_1st'] = temp_array_s[:, 1]
songs['number_lyricist'] = temp_array[:, 2]
songs['lyricist_1st'] = temp_array_s[:, 2]

#%%
# 丢弃原有的歌手作曲作词
songs.drop('artist_name', axis=1, inplace=True)
songs.drop('composer', axis=1, inplace=True)
songs.drop('lyricist', axis=1, inplace=True)

#%%
# 对新增的三个属性和language与length做重编码
cols = ['artist_1st', 'composer_1st', 'lyricist_1st']
for col in cols:
    encoder = LabelEncoder()
    songs[col] = encoder.fit_transform(songs[col])
encoder = LabelEncoder()
songs['language'] = encoder.fit_transform(songs['language'])
songs['song_length'] = np.log1p(songs['song_length'])

#%%
# 读取song_extra_info
path = 'F:\\DataMining\\musicRec\\'
songs_extra = pd.read_csv(path + "song_extra_info.csv")

#%%
# 处理属性：录音统一编码
isrc = songs_extra['isrc']
songs_extra['isrc_country'] = isrc.str.slice(0, 2)
songs_extra['isrc_comp'] = isrc.str.slice(2, 5)
songs_extra['isrc_year'] = isrc.str.slice(5, 7).astype(float)
songs_extra['isrc_year'] = songs_extra['isrc_year'].apply(
    lambda x: 2000 + x if x < 18 else 1900 + x)
#%%
for col in ['isrc_country','isrc_comp','isrc_year']:
    songs_extra[col].fillna('na',inplace=True)
encoder1 = LabelEncoder()
songs_extra['isrc_country'] = encoder1.fit_transform(
    songs_extra['isrc_country'])
encoder2 = LabelEncoder()
songs_extra['isrc_comp'] = encoder2.fit_transform(songs_extra['isrc_comp'])
songs_extra['isrc_missing'] = (songs_extra['isrc_country'] == 0) * 1.0
#%%
# song_cnt
song_cc_cnt = songs_extra.groupby(by='isrc_country').count()[
    'song_id'].to_dict()  # 每个国家代码有多少个歌曲id
song_cc_cnt[0] = None  # 国家码有时是0或not_a_number
songs_extra['isrc_country_song_cnt'] = songs_extra['isrc_country'].apply(
    lambda x: song_cc_cnt[x] if not np.isnan(x) else None)

song_xxx_cnt = songs_extra.groupby(by='isrc_comp').count()['song_id'].to_dict()
song_xxx_cnt[0] = None
songs_extra['isrc_comp_song_cnt'] = songs_extra['isrc_comp'].apply(
    lambda x: song_xxx_cnt[x] if not np.isnan(x) else None)

song_yy_cnt = songs_extra.groupby(by='isrc_year').count()['song_id'].to_dict()
song_yy_cnt[0] = None
songs_extra['isrc_year_song_cnt'] = songs_extra['isrc_year'].apply(
    lambda x: song_yy_cnt[x] if not x is 'na' else None)
#%%
# transform
features = ['isrc_country_song_cnt',
            'isrc_comp_song_cnt', 'isrc_year_song_cnt']
for feat in features:
    songs_extra[feat] = np.log1p(songs_extra[feat])

songs_extra.drop(['name', 'isrc'], axis=1, inplace=True)

#%%
songs=songs.merge(songs_extra, on='song_id', how='left')
#%%
songs.tail()
#%%
songs.columns
#%%
songs_extra.tail()
#%%
len(songs)
songs.to_csv(path + 'songs+extra_pro.csv',index=False)
