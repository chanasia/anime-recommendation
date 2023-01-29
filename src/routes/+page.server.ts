import type { PageServerLoad } from './$types';
import { IP_WEBSITE, PORT_BACKEND } from '$env/static/private';
 
export const load = (async ({ params }) => {
  const ipWebsite = IP_WEBSITE;
  const portBackend = PORT_BACKEND;

  console.log(ipWebsite, " server")

  return {
    ipWebsite,
    portBackend
  }
}) satisfies PageServerLoad;