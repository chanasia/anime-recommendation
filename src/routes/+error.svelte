<script>
  import { page } from '$app/stores';
  import "../app.css"
</script>

<h1>{$page.status}: {$page.error?.message}</h1>
<div>Custom error page</div>
<p>Please contact 12340++</p>