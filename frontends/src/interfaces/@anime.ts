export interface CurrentInfo{
  anime_id: number,
  anime_name: string,
  type: string,
  genre: string | 'NA',
  episodes: number | 'NA',
  rating: number | 'NA',
  members: number,
  title_english: string | 'NA',
  title_japanese: string | 'NA',
  rate: string,
  source: string,
  premiered: string | 'NA',
  studio: string,
  aired: string,
  duration: string
}

export interface SimilarAnimes{
  id: number,
  anime_id: number,
  name: string,
}

export interface SimilarResponse{
  datas:{
    current_info: CurrentInfo,
    similar_animes: SimilarAnimes[]
  }
}

export interface GenreCounts{
    genre: string,
    counts: number
}

export interface GenreLists{
  datas: GenreCounts[]
}

export interface Anime{
  anime_id: number,
  anime_name: string
}

export interface GenresInfo{
  counts: number,
  listanimes: Anime[]
}

export interface GenresRecommand{
  datas: GenresInfo
}

export interface Anime2023{
  datas: Anime[]
}