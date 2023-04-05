import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import type { SimilarResponse,CurrentInfo, SimilarAnimes } from '../../../interfaces/@anime';
import { url } from '$lib/path_url';
// const url = "localhost:5000"

export const load = ( async ({ params, fetch }) => {
  let currentInfo: CurrentInfo;
  let similarAnimes: SimilarAnimes[];

  try{
    const res = await fetch(`${url}/similar_animes/${params.id}`)
    const json = await res.json() as SimilarResponse
    const datas = json.datas
    currentInfo = datas.current_info
    similarAnimes = datas.similar_animes
  }catch{
    throw error(404, 'Not found');
  }

  return {
    currentInfo,
    similarAnimes
  };
}) satisfies PageLoad;
