<script lang="ts">
import '../../../app.css'
import type { SimilarResponse,CurrentInfo, SimilarAnimes } from '../../../interfaces/@anime';
import { error } from '@sveltejs/kit';
import type { PageData } from './$types';
export let data: PageData;
let currentInfo: CurrentInfo;
let similarAnimes: SimilarAnimes[];
import { url } from '$lib/path_url';

$: if(data){
  currentInfo = data.currentInfo
  similarAnimes = data.similarAnimes
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

{#if currentInfo && similarAnimes}
<div style="background-color: #2e3032;">
  <div class="container mx-auto grid md:grid-cols-currentAnime sm:grid-cols-1 gap-8 py-4">
    <div class="md:justify-self-end justify-self-center self-center">
      <img class="w-full object-cover" style="max-width: 225px; height: 325px;" src={`${url}/image/${currentInfo.anime_id}`} alt={currentInfo.anime_name}>
    </div>
    <div class="text-purple-400 tracking-wide">
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Title</span>
        <span>{currentInfo.anime_name}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">English</span>
        <span>{currentInfo.title_english}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Japanese</span>
        <span>{currentInfo.title_japanese}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Type</span>
        <span>{currentInfo.type}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Genre</span>
        <span>{currentInfo.genre}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Rate</span>
        <span>{currentInfo.rate}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Source</span>
        <span>{currentInfo.source}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Studio</span>
        <span>{currentInfo.studio}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Permiered</span>
        <span>{currentInfo.premiered}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Aired</span>
        <span>{currentInfo.aired}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Duration</span>
        <span>{currentInfo.duration}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Episodes</span>
        <span>{currentInfo.episodes}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Rating</span>
        <span>{currentInfo.rating}</span>
      </div>
      <div class="grid grid-cols-labelInfo">
        <span class="text-font-color font-medium">Members</span>
        <span>{(currentInfo.members).toLocaleString()}</span>
      </div>
    </div>
  </div>
</div>
<div class="container mx-auto my-4 text-font-color font-semibold -tracking-tighter text-xl">
  <h1>Recommend  for similar animes <span class="text-main-color">✦</span></h1>
</div>
<div class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-8 2xl:grid-cols-10 container mx-auto select-none">
  {#each similarAnimes as item}
    <a href={`/anime/${item.anime_id}`}>
      <div class="text-font-color flex flex-col tracking-wide relative card" style="width: 100%; max-width: 150px;">
        <div class="overflow-hidden" style="width: 100%; height: 217px; max-width: 150px;">
          <img class="object-cover w-full h-full" src={`${url}/image/${item.anime_id}`} alt={item.name}>
        </div>
        <span class="mt-1 text-overflow">{item.name}</span>
        <span class="text-floating">{item.name}</span>
      </div>
    </a>
  {/each}
</div>
{:else}
<h1>Loading...</h1>
{/if}







