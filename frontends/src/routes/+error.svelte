<script>
  import { page } from '$app/stores';
  import "../app.css"
</script>

<div class="flex justify-center items-center flex-col text-center" style="transform: translateY(-20px); height: 90vh;">
  <h1 class="text-9xl font-bold tracking-tighter text-main-color h-28">{$page.status}</h1>
  <h2 class="text-2xl text-font-color font-medium">{$page.error?.message} {$page.url.pathname}</h2>
  <a href="/" class="text-font-color text-lg bg-neutral-700 p-4 mt-3 rounded-md hover:bg-main-color shadow-lg hover:shadow-main-color/50">Home page</a>
</div>