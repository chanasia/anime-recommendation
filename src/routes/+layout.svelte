<script lang="ts">
  import "../app.css"
  import AutocomplateSearch from "$lib/AutocomplateSearch.svelte"
  import type { PageData } from './$types';

  export let data: PageData;
</script>
<AutocomplateSearch ipWebsite={data.ipWebsite} portBackend={data.portBackend}/>
<slot></slot>
