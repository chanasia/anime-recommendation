import pandas as pd

class AnimeList():
    def __init__(self):
        df_list = pd.read_csv("datasets/animelist2023_dirty.csv")
        self.df_list = df_list.copy()
    
    def get_info(self, anime_id):
        row = self.df_list[self.df_list.anime_id == anime_id]
        if anime_id:
            return {
                "anime_id": int(row.anime_id.values[0]),
                "anime_name": str(row.anime_name.values[0]),
                "type": str(row.type.values[0]),
                "genre": str(row.genre.values[0]),
                "episodes": int(row.episodes.values[0]),
                "rating": float(row.rating.values[0]),
                "members": int(row.members.values[0]),
                "title_english": str(row.title_english.values[0]),
                "title_japanese": str(row.title_japanese.values[0]),
                "rate": str(row.rate.values[0]),
                "source": str(row.source.values[0]),
                "image_url": str(row.image_url.values[0]),
                "premiered": str(row.premiered.values[0]),
                "studio": str(row.studio.values[0]),
                "aired": str(row.aired.values[0]),
                "duration": str(row.duration.values[0]),
            }
        