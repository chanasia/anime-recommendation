<script lang="ts">
import '../app.css'
import Magnify from 'svelte-material-icons/Magnify.svelte'
import type { AnimeResponse, AnimeInfo } from '../interfaces/@autocomplate';
import { debounce } from 'lodash'

let searchTerm:string = '';
let dataJson:AnimeInfo[] = [];

const fetchData = debounce(async (term) => {
  if(searchTerm === '') {
    dataJson = [];
    return;
  }
  try {
    const res = await fetch(`http://127.0.0.1:5000/partial_name/${searchTerm}`)
    const json = await res.json() as AnimeResponse
    dataJson = json.datas
  } catch (error) {
    console.error(error)
  }
}, 500)
</script>

<div class="bg-neutral-800 p-2">
  <div class="container mx-auto">
    <div class="">
      <label class="relative block">
        <span class="sr-only">Search</span>
        <span class="absolute inset-y-0 left-0 flex items-center pl-2">
          <Magnify color="#efef" width={25} height={25}/>
        </span>
        <input class="placeholder:text-zinc-400 block bg-inputText-color w-full border-2 border-inputText-color text-font-color rounded-md py-2 pl-9 pr-3 shadow-sm focus:outline-none focus:border-main-color" placeholder="Search for anything..." type="text" name="search" bind:value={searchTerm} on:input={fetchData}/>
      </label>
    </div>
  </div>
</div>
{#if dataJson !== null}
  {#each dataJson as suggestion}
    <div>
      <img src={`http://127.0.0.1:5000/image/${suggestion.anime_id}`} alt={suggestion.name}>
      {suggestion.name}
    </div>
  {/each}
{/if}