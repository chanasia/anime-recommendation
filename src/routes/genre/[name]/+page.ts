import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

const url = "localhost:5000"
interface Datas{
  datas: number
}

export const load = ( async ({ params, fetch }) => {
  let counts:number;

  try{
    const res = await fetch(`http://${url}/get_genre_counts/${params.name}`)
    const json = await res.json() as Datas
    counts = json.datas
  }catch{
    throw error(404, 'Not found');
  }

  return {
    genreName: params.name,
    counts
  };
}) satisfies PageLoad;
