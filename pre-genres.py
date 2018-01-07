#%%
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

#%%
# 读取songs文件的曲风列。
path = 'F:\\DataMining\\musicRec\\'
song_genre = pd.read_csv(path + "songs.csv")
#                         ,usecols=['genre_ids'])  # , skiprows=lambda x: x > 60)

#%%
temp_array = np.zeros((len(song_genre), 4))
for i in range(len(song_genre)):
    x = song_genre['genre_ids'].values[i]
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
song_genre['genre_count'] = temp_array[:, 0]
song_genre['genre_1st'] = temp_array[:, 1]
song_genre['genre_2nd'] = temp_array[:, 2]
song_genre['genre_3rd'] = temp_array[:, 3]

#%%
genre_encoder = LabelEncoder()
genre_encoder.fit((song_genre.genre_1st.append(
    song_genre.genre_2nd)).append(song_genre.genre_3rd))
song_genre['genre_1st'] = genre_encoder.transform(song_genre['genre_1st'])
song_genre['genre_2nd'] = genre_encoder.transform(song_genre['genre_2nd'])
song_genre['genre_3rd'] = genre_encoder.transform(song_genre['genre_3rd'])
song_genre.drop('genre_ids', axis=1, inplace=True)

'''
# 别跑这一个
song_genre.drop('genre_ids', axis=1, inplace=True)
songs = pd.read_csv(path + "songs.csv")
songs.join(song_genre)
songs.to_csv(path + 'songs_genre.csv')
'''
#%%
song_genre.tail()
#%%
song_genre.columns
#%%
'''
提取歌手、作词、作曲的数量与首席是什么。
'''


def get_acl_count_name(x, filter):
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


'''
x = 'one;twoandthree+four'
filter = [';', 'and', '+']
print(get_acl_count_name(x, filter)[1])
'''
len_song_genre = len(song_genre)
temp_array = np.zeros((len_song_genre, 3))
temp_array_s = np.empty((len_song_genre, 3), '<U10')
filter1 = ['and', '&', 'feat']
filter2 = ['\\', '|', '/']
for col in ['artist_name', 'composer', 'lyricist']:
    song_genre[col].fillna('')
for i in range(len_song_genre):
    (count, name) = get_acl_count_name(
        song_genre['artist_name'].values[i], filter1)
    temp_array[i, 0] = count
    temp_array_s[i, 0] = name
    (count, name) = get_acl_count_name(
        song_genre['composer'].values[i], filter2)
    temp_array[i, 1] = count
    temp_array_s[i, 1] = name
    (count, name) = get_acl_count_name(
        song_genre['lyricist'].values[i], filter2)
    temp_array[i, 2] = count
    temp_array_s[i, 2] = name

for j in range(3):
    encoder = LabelEncoder()
    temp_array_s[:, j] = encoder.fit_transform(temp_array[:, j])

song_genre['number_artist'] = temp_array[:, 0]
song_genre['artist_1st'] = temp_array_s[:, 0]
song_genre['number_composer'] = temp_array[:, 1]
song_genre['composer_1st'] = temp_array_s[:, 1]
song_genre['number_lyricist'] = temp_array[:, 2]
song_genre['lyricist_1st'] = temp_array_s[:, 2]

#%%
## 对新增的三个属性做重编码
cols = ['artist_1st', 'composer_1st', 'lyricist_1st']
for col in cols:
    encoder = LabelEncoder()
    song_genre[col] = encoder.fit_transform(song_genre[col])

#%%
len(song_genre)
song_genre.to_csv(path + 'songs_genre.csv')
