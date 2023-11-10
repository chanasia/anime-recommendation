<script lang="ts">
import '../app.css'
import Magnify from 'svelte-material-icons/Magnify.svelte'
import Github from 'svelte-material-icons/Github.svelte'
import type { AnimeResponse, AnimeInfo } from '../interfaces/@autocomplate';
import { url } from './path_url';
import pkg from 'lodash'
const { debounce } = pkg

// const url = 'localhost:5000'

let searchTerm:string = '';
let dataJson:AnimeInfo[] = [];
let isHidden:boolean = true;

const onFocus = () => setTimeout(() => isHidden = false, 100)
const lostFocus = () => setTimeout(() => isHidden = true, 300)

const fetchData = debounce(async () => {
  if(searchTerm === '') {
    dataJson = [];
    return;
  }
  try {
    const res = await fetch(`${url}/partial_name/${searchTerm}`)
    const json = await res.json() as AnimeResponse
    dataJson = json.datas
  } catch (error) {
    console.error(error)
  }
}, 1000)

fetchData()

let inputWidth: number;

const handleResize = (event: UIEvent) => {
  console.log((event.target as Window).innerWidth)
  // ...
};
// document.addEventListener("resize", handleResize);
</script>

<style>
  .hidden{
    display: none;
  }
</style>
<div class="bg-neutral-800 p-2 shadow-lg">
  <div class="container mx-auto grid gap-4" style="grid-template-columns: 1fr 2fr 1fr; ">
    <a href="/" class="justify-self-end flex items-center">
      <h1 class="text-main-color font-bold text-3xl">RengMe!</h1>
    </a>
    <div class="flex justify-center">
      <label class="relative block">
        <span class="sr-only">Search</span>
        <span class="absolute inset-y-0 left-0 flex items-center pl-2">
          <Magnify color="#efef" width={25} height={25}/>
        </span>
        <input class="placeholder:text-zinc-400 block bg-inputText-color xl:w-160 lg:w-128 md:w-96 w-72 border-2 border-inputText-color text-font-color rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-main-color" placeholder="Search for anything..." type="text" name="search" bind:value={searchTerm} on:input={fetchData} on:focus={onFocus} on:blur={lostFocus} on:resize={handleResize} />
      </label>
      <ul class="select-none absolute translate-y-2 bg-inputText2-color z-20" style="top: 45px" class:hidden={isHidden}>
        {#if dataJson !== null}
          {#each dataJson as suggestion}
            <li class="xl:w-160 lg:w-128 md:w-96 w-72 py-1 px-2  hover:cursor-pointer text-font-color hover:text-main-color ease-out duration-100">
              <a href={`/anime/${suggestion.anime_id}`} class="flex items-center">
                <img style="width: 32px; height:45px;" src={`${url}/image/${suggestion.anime_id}`} alt={suggestion.name} draggable="false">
                <span class="ml-2">{suggestion.name}</span>
              </a>
            </li>
          {/each}
        {/if}
      </ul>
    </div>
    <a href="https://github.com/chanasia/anime-recommendation">
      <Github color="#efef" width={40} height={40}/>
    </a>
  </div>
</div>

