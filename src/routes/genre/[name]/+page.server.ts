import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { IP_WEBSITE, PORT_BACKEND } from '$env/static/private';

interface Datas{
  datas: number
}

export const load = ( async ({ params, fetch }) => {
  let counts:number;

  try{
    const res = await fetch(`http://${IP_WEBSITE}:${PORT_BACKEND}/get_genre_counts/${params.name}`)
    const json = await res.json() as Datas
    counts = json.datas
  }catch{
    throw error(404, 'Not found');
  }

  return {
    genreName: params.name,
    counts
  };
}) satisfies PageServerLoad;
