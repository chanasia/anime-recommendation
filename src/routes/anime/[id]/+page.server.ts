import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { SimilarResponse,CurrentInfo, SimilarAnimes } from '../../../interfaces/@anime';
import { IP_WEBSITE, PORT_BACKEND } from '$env/static/private';

export const load = ( async ({ params, fetch }) => {
  let currentInfo: CurrentInfo;
  let similarAnimes: SimilarAnimes[];

  try{
    const res = await fetch(`http://${IP_WEBSITE}:${PORT_BACKEND}/similar_animes/${params.id}`)
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
}) satisfies PageServerLoad;
