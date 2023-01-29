import type { LayoutServerLoad } from './$types';
import { IP_WEBSITE, PORT_BACKEND } from '$env/static/private';
 
export const load = (async ({ params }) => {
  const ipWebsite = IP_WEBSITE;
  const portBackend = PORT_BACKEND;

  return {
    ipWebsite,
    portBackend
  }
}) satisfies LayoutServerLoad;