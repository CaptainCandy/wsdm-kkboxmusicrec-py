#%%
import pandas as pd
import numpy as np

#%%
# 读取songs文件的曲风列。
path = 'F:\\DataMining\\musicRec\\'
song_genre = pd.read_csv(path + "songs.csv",
                         usecols=['genre_ids'], skiprows=lambda x: x > 60)

#%%
# type(str(song_genre['genre_ids'].values[1]).split('|'))
# type(np.zeros((40, 3)))
isinstance(song_genre['genre_ids'].values[1], str)
i = 1
x = song_genre['genre_ids'].values[i]
for i in range(1):
    if not isinstance(x, str):
        print(x)
        continue
    print(555)
len(song_genre)

#%%
temp_array = np.zeros((len(song_genre), 4))
for i in range(len(song_genre)):
    x = song_genre['genre_ids'].values[i]
    if not isinstance(x, str):
        print(x)
        continue
    list_id = str(x).split('|')
    # song_genre.loc[i, 'genre_count'] = len(list_id)
    temp_array[i, 0] = len(list_id)
    if len(list_id) > 0:
        temp_array[i, 1] = int(list_id[0])
        if len(list_id) > 1:
            temp_array[i, 2] = int(list_id[1])
            if len(list_id) > 2:
                temp_array[i, 3] = int(list_id[2])
song_genre['genre_count'] = temp_array[:, 0]
song_genre['genre_1st'] = temp_array[:, 1]
song_genre['genre_2nd'] = temp_array[:, 2]
song_genre['genre_3rd'] = temp_array[:, 3]


@staticmethod
def process_genre_ids(df, col):
    for i in range(len(df)):
        if not isinstance(df[col].values)
