export interface AnimeInfo{
  anime_id: number;
  // id: number;
  name: string;
}

export interface AnimeResponse{
  datas: AnimeInfo[];
}