<script lang="ts">
import "../app.css"
import GenresSelection from "$lib/GenresSelection.svelte";
import type { PageData } from './$types';
import GenreRecommend from "$lib/GenreRecommend.svelte";

export let data: PageData

let genreSelected: string;

const genreArray: string[] = ['Adventure', 'Fantasy', 'Comedy', 'Action', 'School', 'Shounen', 'Isekai', 'Romance', 'Sci-Fi', 'Drama', 'Mahou Shoujo', 'Psychological', 'Survival', 'Shoujo', 'Vampire', 'Horror', 'Supernatural'];

let randomGenre: string = genreArray[Math.floor(Math.random() * genreArray.length)]
</script>

<GenresSelection ipWebsite={data.ipWebsite} portBackend={data.portBackend} bind:genreSelected/>

{#if genreSelected}
  <div class="container mx-auto my-4 text-font-color font-semibold -tracking-tighter text-xl">
    <h1>Recommend {genreSelected} animes <span class="text-main-color">✦</span></h1>
  </div>
  <GenreRecommend genreSelected={genreSelected} ipWebsite={data.ipWebsite} portBackend={data.portBackend}/>
{:else}
  <div class="container mx-auto my-4 text-font-color font-semibold -tracking-tighter text-xl">
    <h1>Recommend {randomGenre} animes <span class="text-main-color">✦</span></h1>
  </div> 
  <GenreRecommend genreSelected={randomGenre} ipWebsite={data.ipWebsite} portBackend={data.portBackend}/>
{/if}

