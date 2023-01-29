<script lang="ts">
import '../app.css'
import Magnify from 'svelte-material-icons/Magnify.svelte'
import type { AnimeResponse, AnimeInfo } from '../interfaces/@autocomplate';
import pkg from 'lodash'
const { debounce } = pkg
export let ipWebsite: string;
export let portBackend: string;

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
    const res = await fetch(`http://${ipWebsite}:${portBackend}/partial_name/${searchTerm}`)
    const json = await res.json() as AnimeResponse
    dataJson = json.datas
  } catch (error) {
    console.error(error)
  }
}, 1000)

fetchData()
</script>

<style>
  .hidden{
    display: none;
  }
</style>
<div class="bg-neutral-800 p-2 shadow-lg">
  <div class="container mx-auto flex justify-center">
    <div>
      <label class="relative block">
        <span class="sr-only">Search</span>
        <span class="absolute inset-y-0 left-0 flex items-center pl-2">
          <Magnify color="#efef" width={25} height={25}/>
        </span>
        <input class="placeholder:text-zinc-400 block bg-inputText-color lg:w-96  md:w-80 w-72 border-2 border-inputText-color text-font-color rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-main-color" placeholder="Search for anything..." type="text" name="search" bind:value={searchTerm} on:input={fetchData} on:focus={onFocus} on:blur={lostFocus} />
      </label>
      <ul class="select-none absolute translate-y-2 bg-inputText2-color z-20" class:hidden={isHidden}>
        {#if dataJson !== null}
          {#each dataJson as suggestion}
            <li class="lg:w-96 md:w-80 w-72 py-1 px-2  hover:cursor-pointer text-font-color hover:text-main-color ease-out duration-100">
              <a href={`/anime/${suggestion.anime_id}`} class="flex items-center">
                <img style="width: 32px; height:45px;" src={`http://${ipWebsite}:${portBackend}/image/${suggestion.anime_id}`} alt={suggestion.name} draggable="false">
                <span class="ml-2">{suggestion.name}</span>
              </a>
            </li>
          {/each}
        {/if}
      </ul>
    </div>
  </div>
</div>

