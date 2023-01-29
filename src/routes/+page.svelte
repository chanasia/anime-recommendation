<script lang="ts">
import "../app.css"
import GenresSelection from "$lib/GenresSelection.svelte";
import type { PageData } from './$types';
import GenreRecommend from "$lib/GenreRecommend.svelte";

export let data: PageData

let genreSelected: string;
</script>

<GenresSelection ipWebsite={data.ipWebsite} portBackend={data.portBackend} bind:genreSelected/>

{#if genreSelected}
  <h1>{genreSelected}</h1>
  <GenreRecommend genreSelected={genreSelected} ipWebsite={data.ipWebsite} portBackend={data.portBackend}/>
{/if}

