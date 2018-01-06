#%%
import pandas as pd
import numpy as np

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
        print(x)
        continue
    list_id = str(x).split('|')
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
'''
#%% 别跑这一个
song_genre.drop('genre_ids', axis=1, inplace=True)
songs = pd.read_csv(path + "songs.csv")
songs.join(song_genre)
songs.to_csv(path + 'songs_genre.csv')
'''
#%%
len(song_genre)
song_genre.to_csv(path + 'songs_genre.csv')
