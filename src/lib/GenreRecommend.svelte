<script lang="ts">
import pkg from 'lodash'
const { debounce } = pkg
import type { GenresRecommand, GenresInfo, Anime} from '../interfaces/@anime';
import { url } from './path_url';

export let genreSelected: string;
// const url = 'localhost:5000'

let listanimes: Anime[] = [];
let counts: number;

const fetchData = debounce(async () => {
  try{
    const res = await fetch(`${url}/get_anime_match_genre/${genreSelected}`)
    const json = await res.json() as GenresRecommand
    const dataJson: GenresInfo = json.datas
    listanimes = dataJson.listanimes
    counts = dataJson.counts
  }catch (error) {
    console.error(error)
  }
}, 300)

$: if(genreSelected){
  fetchData()
}
</script>

<style>
  .text-overflow {
    /* white-space: nowrap; */
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    /* position: relative; */
    z-index: 0;
  }

  .text-floating{
    /* display: none; */
    opacity: 0;
    position: absolute;
    background: rgb(255, 255, 255);
    color: #333;
    font-size: 10px;
    white-space: pre-wrap;
    width: 150;
    border-radius: 3px;
    padding: 0 3px;
    bottom: 55px;
    right: 0;
    z-index: 10;
  }

  .text-overflow:hover + .text-floating {
    /* display: block; */
    transition-delay: 2s;
    transition-property: opacity;
    opacity: 1;
  }

  .card img{
    transition: transform .3s;
  }

  .card:hover img{
    transform: scale(1.2);
  }
</style>

<div class="container mx-auto select-none">
  <div class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-8 2xl:grid-cols-10">
    {#each listanimes as item}
      <a href={`/anime/${item.anime_id}`}>
        <div class="text-font-color flex flex-col tracking-wide relative card" style="width: 100%; max-width: 150px;">
          <div class="overflow-hidden" style="width: 100%; height: 217px; max-width: 150px;">
            <img class="object-cover w-full h-full" src={`${url}/image/${item.anime_id}`} alt={item.anime_name}>
          </div>
          <span class="mt-1 text-overflow">{item.anime_name}</span>
          <span class="text-floating">{item.anime_name}</span>
        </div>
      </a>
    {/each}
  </div>
  <div class="flex justify-end">
    <a class="text-font-color underline hover:text-main-color mt-2" href={`genre/${genreSelected}`}>{counts} {genreSelected} anime, click!</a>
  </div>
</div>