<script lang="ts">
import '../app.css'
import type { GenreCounts, GenreLists } from '../interfaces/@anime';
import pkg from 'lodash'
const { debounce } = pkg
import ChevronRight from 'svelte-material-icons/ChevronRight.svelte'
import ChevronLeft from 'svelte-material-icons/ChevronLeft.svelte'
import { onMount, onDestroy } from 'svelte';
import { url } from './path_url';

export let genreSelected: string;
// const url = 'http://localhost:5000'

let dataJson: GenreCounts[] = [];

const fetchData = debounce(async () => {
  try {
    const res = await fetch(`${url}/genre_lists/`)
    const json = await res.json() as GenreLists
    dataJson = json.datas
  } catch (error) {
    console.error(error)
  }
}, 100)

fetchData()

let scrollContainer: HTMLElement;
let leftButtonHidden = true;
let rightButtonHidden = false;

function handleScroll() {
  const { scrollLeft, scrollWidth, clientWidth } = scrollContainer;
  leftButtonHidden = scrollLeft === 0;
  rightButtonHidden = scrollWidth - scrollLeft === clientWidth;
}

onMount(() => {
  scrollContainer.scrollLeft = 0;
  if (scrollContainer) {
    scrollContainer.addEventListener('scroll', handleScroll);
  }
});

onDestroy(() => {
  if (scrollContainer) {
    scrollContainer.removeEventListener('scroll', handleScroll);
  }
});


function scrollLeft() {
  scrollContainer.scrollLeft -= 300;
}

function scrollRight() {
  scrollContainer.scrollLeft += 300;
}

function onClickGenre(e: Event){
 genreSelected = String((e.target as HTMLElement).textContent)
}
</script>

<style>
  .hiddenArrow {
    display: none;
  }

  .scroll-container::-webkit-scrollbar {
  width: 0;
  height: 0;
  background: transparent;
}
</style>

{#if dataJson}
<div class="container mx-auto mt-4 text-font-color relative">
  <div class="flex flex-row flex-nowrap gap-1 overflow-hidden overflow-x-scroll scroll-container scroll-smooth select-none" bind:this={scrollContainer}>
    {#each dataJson as item}
    <button class="whitespace-nowrap px-3 py-1 rounded-xl bg-zinc-700 transition-colors duration-100 hover:bg-neutral-800 hover:text-main-color  shadow-md hover:shadow-lg" on:click={onClickGenre}>{item.genre}</button>
    {/each}
  </div>
  <button class="absolute left-0 w-20  flex justify-start items-center" style="top: -10px; background-image: linear-gradient(90deg, rgba(55,58,60,1) 0%, rgba(55,58,60,1) 75%, rgba(2,0,36,0) 100%); width: 50px; height: 50px;" on:click={scrollLeft} class:hiddenArrow={leftButtonHidden}><ChevronLeft color="#efef" width={40} height={40}/></button>

  <button class="absolute right-0 w-20 flex justify-end items-center" style="top: -10px; background-image: linear-gradient(90deg, rgba(2,0,36,0) 0%, rgba(55,58,60,1) 25%, rgba(55,58,60,1) 100%); width: 50px; height: 50px;" on:click={scrollRight} class:hiddenArrow={rightButtonHidden}><ChevronRight color="#efef" width={40} height={40}/></button>
</div>
{/if}
