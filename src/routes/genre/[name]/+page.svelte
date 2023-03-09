<script lang='ts'>
import '../../../app.css'
import type { PageData } from './$types';
import type { Anime } from '../../../interfaces/@anime';
import { onMount } from 'svelte';
import { url } from '$lib/path_url';

export let data: PageData
// const url = "localhost:5000"
interface Datas{
  datas: Anime[]
}


let genreName = data.genreName;
let counts = data.counts;
let stopScrollPage = false;

let dataJson:Anime[] = [];
let page = 1;

async function fetchData() {
  try{
    const response = await fetch(`${url}/genre/?name=${genreName}&page=${page}`);
    const json = await response.json() as Datas;
    dataJson = [...dataJson, ...json.datas];
  }catch (error) {
    stopScrollPage = true
  }
}

fetchData()

let scrollY: number;

function handleScroll() {
  if(stopScrollPage) return
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    page++;
    fetchData();
  }
}

onMount(() => {
  // handleScroll()
})

$: if(scrollY) handleScroll()
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

<div class="container mx-auto my-4 text-font-color font-semibold -tracking-tighter text-xl">
  <h1>{counts} for {genreName} animes <span class="text-main-color">✦</span></h1>
</div>
<svelte:window bind:scrollY={scrollY}/>
<div class="container mx-auto select-none">
  <div class="grid grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-8 2xl:grid-cols-10">
    {#each dataJson as item}
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
</div>
