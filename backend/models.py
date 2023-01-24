import re
import pandas as pd
import numpy as np

class AnimeModels:
    def __init__(self):
        print("Loading datasets..")
        df_anime = pd.read_csv("datasets/animelist2023_filter.csv")

        self.df_anime = df_anime.copy()
        self.all_anime_names = list(df_anime.anime_name.values)
        self.all_anime_ids = list(df_anime.anime_id.values)

        print("Loading models..")

        self.indices = np.load('models/indices.npy')

        print('Complete datasets, model loaded!')
    
    def search_partial_name(self, partial):
        return [ {
            "id": self.all_anime_names.index(name), 
            "anime_id": int(self.df_anime.iloc[id].anime_id), 
            "name":name
            } \
             for id, name in enumerate(self.all_anime_names) if str.lower(partial) in str.lower(name)]

    def similar_animes(self, id):
        
        return [ { 
                "id": int(idx),
                "anime_id": int(self.df_anime.iloc[idx].anime_id),
                "name": str(self.df_anime.iloc[idx].anime_name)
            } for idx in self.indices[id][1:]]



