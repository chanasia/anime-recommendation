import pandas as pd
import numpy as np

class AnimeList():
    def __init__(self):
        print("Loading datasets..")
        df_anime = pd.read_csv("datasets/animelist2023_clean.csv")
        df_list = pd.read_csv("datasets/animelist2023_dirty.csv")
        genre = pd.Series(df_anime.genre.str.split(", ", expand=True).stack().value_counts().index.tolist())
        count = pd.Series(df_anime.genre.str.split(", ", expand=True).stack().value_counts().values.tolist())

        self.df_list = df_list.copy()
        self.df_anime = df_anime.copy()
        self.all_anime_names = list(df_anime.anime_name.values)
        self.all_anime_ids = list(df_anime.anime_id.values)
        self.genre_lists = pd.DataFrame(data={'genre': genre, "counts": count})
        self.df_anime2023 = df_anime.copy()

        self.df_anime2023.aired = self.df_anime2023.aired.str.extract(r'(\d{4})')
        self.df_anime2023.aired = self.df_anime2023.aired.fillna(0)
        self.df_anime2023.aired = self.df_anime2023.aired.astype(int)
        self.df_anime2023 = (self.df_anime2023[self.df_anime2023.aired.isin([2023])].sort_values(by="rating", ascending=False)).reset_index(drop=True)

        print("Loading models..")

        self.indices = np.load('models/indices.npy')

        print('Complete datasets, model loaded!')


    def search_partial_name(self, partial):
        return [ {
            "anime_id": int(self.df_anime.iloc[id].anime_id), 
            "name":name
            } \
                for id, name in enumerate(self.all_anime_names) if str.lower(partial) in str.lower(name)][:10]

    def similar_animes(self, anime_id):
        row = self.df_anime[self.df_anime.anime_id == anime_id]
        if(len(row.index.values) != 0):
            id = row.index.values[0]
            return [ { 
                    "anime_id": int(self.df_anime.iloc[idx].anime_id),
                    "name": str(self.df_anime.iloc[idx].anime_name),
                } for idx in self.indices[id][1:]]

    def get_info(self, anime_id):
        row = self.df_list[self.df_list.anime_id == anime_id]
        if(len(row.index.values) != 0):
            return {
                "anime_id": anime_id,
                "anime_name": str(row.anime_name.values[0]),
                "type": str(row.type.values[0]),
                "genre": 'NA' if row.genre.isna().any() else str(row.genre.values[0]),
                "episodes": 'NA' if row.episodes.isna().any() else int(row.episodes.values[0]),
                "rating": 'NA' if row.rating.isna().any() else float(row.rating.values[0]),
                "members": int(row.members.values[0]),
                "title_english": 'NA' if row.title_english.isna().any() else str(row.title_english.values[0]),
                "title_japanese": 'NA' if row.title_japanese.isna().any() else str(row.title_japanese.values[0]),
                "rate": str(row.rate.values[0]),
                "source": str(row.source.values[0]),
                "premiered": 'NA' if row.premiered.isna().any() else str(row.premiered.values[0]),
                "studio": str(row.studio.values[0]),
                "aired": str(row.aired.values[0]),
                "duration": str(row.duration.values[0]),
                }
                
    def get_genre_list(self):
        return list(self.genre_lists.to_dict(orient='records'))

    def is_genre_list_names(self, genre_name): # return ture or false
        return True if (len([item for item in self.genre_lists.genre.values.tolist() if str.lower(genre_name) in str.lower(item)]) != 0) else False

    def get_anime_match_genre(self, genre_selected):
        if(self.is_genre_list_names(genre_selected)):
            genre_match = self.df_anime.genre.apply(lambda x: True if len([item for item in x.split(", ") if item in genre_selected]) != 0 else False)
            df_match = (self.df_anime.loc[genre_match[genre_match.values == True].index].sort_values(by='rating', ascending=False).head(100)).sample(frac=1)

            return list((df_match[['anime_id', 'anime_name']].head(10)).to_dict(orient='records'))

    def get_genre_counts(self, genre_name):
        return int(self.genre_lists[self.genre_lists.genre == genre_name].counts.values[0])

    def get_genre_with_page(self, genre_selected, page):
        if(self.is_genre_list_names(genre_selected)):
            if(page == 1): limit = 30
            else: limit = 10
            start_index = (page-1)*limit
            end_index = page*limit-1
            genreMatch = self.df_anime.genre.apply(lambda x: True if len([item for item in x.split(", ") if item in genre_selected]) != 0 else False)
            df_match = (self.df_anime.loc[genreMatch[genreMatch.values == True].index].sort_values(by='rating', ascending=False)).reset_index(drop=True)
            if len(df_match.loc[start_index:end_index].values) != 0:
                df_page = df_match.loc[start_index:end_index]
                return df_page[['anime_id', 'anime_name']].to_dict(orient='records')
        
    
    def get_anime_2023_with_page(self, page):
        if page == 0:
            page = 1
            limit = 10
        elif page == 1: limit = 30
        else: limit = 10
        start_index = (page-1)*limit
        end_index = page*limit-1
        if len(self.df_anime2023.loc[start_index:end_index]) != 0:
            df_page = self.df_anime2023.loc[start_index:end_index]
            return df_page[['anime_id', 'anime_name']].to_dict(orient='records')

