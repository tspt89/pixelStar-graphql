from django.shortcuts import render

import redis as redis
from django.http import HttpResponse, JsonResponse
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

r = redis.StrictRedis(host='104.198.244.0', port=6379,	charset="utf-8",decode_responses=True)

# Create your views here.
def redis(request):
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22af8a2d155b479ba6971680d903d894",
															   client_secret="e75127b7d9244deeb95385fc825715cf"))
	array = []

	if r.exists("top") == 0:
		print("No existe la lista","Obteniendo query de spotify",sep="\n")
		results = sp.playlist('spotify:playlist:3WxTnGherpf7t4F0VzchD4')

		print("Asociando nombres, y guardando en query de redis: top")
		for idx, track in enumerate(results['tracks']['items']):
			res = {'name': track['track']['name'],
				   'artist': track['track']['artists'][0]['name'],
				   'album': track['track']['album']['name'],
				   'release': track['track']['album']['release_date'],
				   'duration': track['track']['duration_ms']
				   }
			r.rpush('top', track['track']['name'])
			r.hmset(track['track']['name'], res);
			array.append(res)

	else:
		print("La lista si existe")
		namePlaylist = r.lrange("top",0,-1)
		for name in namePlaylist:
			res = r.hgetall(name)
			array.append(res)


	return JsonResponse(array, safe = False, json_dumps_params={'ensure_ascii': False})

	
def topGenero(request):
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22af8a2d155b479ba6971680d903d894",
															   client_secret="e75127b7d9244deeb95385fc825715cf"))
	array = []

	print(request)

	if r.exists("topGenero") == 0:
		print("No existe la lista","Obteniendo query de spotify",sep="\n")
		results = sp.playlist('spotify:playlist:37i9dQZF1DX92MLsP3K1fI')

		print("Asociando nombres, y guardando en query de redis: topGenero")
		for idx, track in enumerate(results['tracks']['items']):
			res = {'name': track['track']['name'],
				   'artist': track['track']['artists'][0]['name'],
				   'album': track['track']['album']['name'],
				   'release': track['track']['album']['release_date'],
				   'duration': track['track']['duration_ms']
				   }
			r.rpush('topGenero', track['track']['name'])
			r.hmset(track['track']['name'], res);
			array.append(res)

	else:
		print("La lista si existe")
		namePlaylist = r.lrange("topGenero",0,-1)
		for name in namePlaylist:
			res = r.hgetall(name)
			array.append(res)


	return JsonResponse(array, safe = False, json_dumps_params={'ensure_ascii': False})