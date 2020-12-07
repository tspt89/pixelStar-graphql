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

def topArtistas(request):
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22af8a2d155b479ba6971680d903d894",
															   client_secret="e75127b7d9244deeb95385fc825715cf"))
	array = []

	if r.exists("topArtistas") == 0:
		print("No existe la lista","Obteniendo query de spotify",sep="\n")
		
		results = sp.artists(['spotify:artist:6eUKZXaKkcviH0Ku9w2n3V', 'spotify:artist:66CXWjxzNUsdJxJ2JdwvnR', 'spotify:artist:3TVXtAsR1Inumwj472S9r4', 'spotify:artist:5pKCCKE2ajJHZ9KAiaK11H', 'spotify:artist:1uNFoZAHBGtllmzznpCI3s', 'spotify:artist:7dGJo4pcD2V6oG8kP0tJRR', 'spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH', 'spotify:artist:06HL4z0CvFAxyc27GXpf02', 'spotify:artist:53XhwfbYqKCa1cC15pYq2q', 'spotify:artist:1dfeR4HaWDbWqFHLkxsg1d', 'spotify:artist:7n2wHs1TKAczGzO7Dd2rGr', 'spotify:artist:246dkjvS1zLTtiykXe5h60', 'spotify:artist:64KEffDW9EtZ1y2vBYgq8T', 'spotify:artist:04gDigrS5kc9YWfZHwBETP', 'spotify:artist:4gzpq5DPGxSnKTe4SA8HAU', 'spotify:artist:0du5cEVh5yTK9QJze8zA0C', 'spotify:artist:4q3ewBCX7sLwd24euuV69X', 'spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ', 'spotify:artist:3Nrfpe0tUJi4K4DXYWgMUX', 'spotify:artist:7vk5e3vY1uw9plTHJAMwjN', 'spotify:artist:1i8SpTcr7yvPOmcqrbnVXY', 'spotify:artist:6vWDO969PvNqNYHIOW5v0m', 'spotify:artist:4dpARuHxo51G3z768sgnrY', 'spotify:artist:1vyhD5VmyZ7KMfW5gqLgo5', 'spotify:artist:0C8ZW7ezQVs4URX5aX7Kqx', 'spotify:artist:4nDoRrQiYLoBzwC5BhVJzF'])

		print("Asociando nombres, y guardando en query de redis: topArtistas")

		for idx, artists in enumerate(results['artists']):
			res = {'name': artists['name'],
				   'followers': artists['followers']['total'],
				   'popularity': artists['popularity'],
				   'genre': artists['genres'][0],
				   }
			r.rpush('topArtistas', artists['name'])
			r.hmset(artists['name'], res);
			array.append(res)

	else:
		print("La lista si existe")
		namePlaylist = r.lrange("topArtistas",0,-1)
		for name in namePlaylist:
			res = r.hgetall(name)
			array.append(res)

	return JsonResponse(array, safe = False, json_dumps_params={'ensure_ascii': False})


def topDiscos(request):
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22af8a2d155b479ba6971680d903d894",
															   client_secret="e75127b7d9244deeb95385fc825715cf"))
	array = []

	if r.exists("topDiscos") == 0:
		print("No existe la lista","Obteniendo query de spotify",sep="\n")
		
		disco = sp.albums(['spotify:album:5lJqux7orBlA1QzyiBGti1', 'spotify:album:4yP0hdKOZPNshxUOjY0cZj', 'spotify:album:5XCBX16KNYsAe7V5hQV9mC', 'spotify:album:7fJJK56U9fHixgO0HQkhtI', 'spotify:album:68enXe5XcJdciSDAZr0Alr', 'spotify:album:6mJZTV8lCqnwftYZa94bXS', 'spotify:album:7JtT7OyWM8BnIS5FXXPMKg', 'spotify:album:26c7MmQ4w8EAvVLb4jilaM', 'spotify:album:6n9DKpOxwifT5hOXtgLZSL', 'spotify:album:6EgJXcGqaUvgZIF9bqPXfP', 'spotify:album:63iWSELt9V1kV6RSMxN7Ii', 'spotify:album:0fEO7g2c5onkaXsybEtuD2', 'spotify:album:2mX8ktJoWvyidWBU9U8Jis', 'spotify:album:5obQ9rPASQW2mLxYM8Ko6Z', 'spotify:album:623PL2MBg50Br5dLXC9E9e', 'spotify:album:4otkd9As6YaxxEkIjXPiZ6', 'spotify:album:1BBjdKgGAqwdEvcvqBOGfT', 'spotify:album:1pzvBxYgT6OVwJLtHkrdQK', 'spotify:album:6xS6mQz1fQZ6eZE654J15I', 'spotify:album:45c1tgTktunRMmfh3WVh8U'])

		print("Asociando nombres, y guardando en query de redis: topDiscos")

		for idx, albums in enumerate(disco['albums']):
			res = {'name': albums['name'],
				   'artist': albums['artists'][0]['name'],
				   'popularity': albums['popularity'],
				   'release': albums['release_date'],
				   }
			r.rpush('topDiscos', albums['name'])
			r.hmset(albums['name'], res);
			array.append(res)

	else:
		print("La lista si existe")
		namePlaylist = r.lrange("topDiscos",0,-1)
		for name in namePlaylist:
			res = r.hgetall(name)
			array.append(res)

	#print(albums['name'], albums['artists'][0]['name'], albums['popularity'], albums['release_date'])

	return JsonResponse(array, safe = False, json_dumps_params={'ensure_ascii': False})

def prediction(request):
    import spotipy
    import pandas as pd #Dataframe, Series
    from sklearn.model_selection import train_test_split
    from spotipy.oauth2 import SpotifyClientCredentials
    from sklearn.metrics import accuracy_score

    data = pd.read_csv('pixelstarmusic/data.csv')

    print(data.describe())
    print(data.info())

    train, test = train_test_split(data, test_size = 0.15)

    features = ["danceability", "loudness", "valence", "energy", "instrumentalness", "acousticness", "key", "speechiness","duration_ms"]
    print("Training size: {}, Test size: {}".format(len(train),len(test)))

    x_train = train[features]
    y_train = train["target"]

    x_test = test[features]
    y_test = test["target"]


    from sklearn.ensemble import GradientBoostingClassifier
    gbc = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
    gbc.fit(x_train, y_train)
    predicted = gbc.predict(x_test)
    score = accuracy_score(y_test, predicted)*100
    print("Accuracy using Gbc: ", round(score, 1), "%")

    test = pd.read_csv('pixelstarmusic/indie.csv')

    new_test_data = test[features]
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="22af8a2d155b479ba6971680d903d894",
                                                                   client_secret="e75127b7d9244deeb95385fc825715cf"))

    pred = gbc.predict(new_test_data)

    likedSongs = 0
    i = 0
    arr = []
    for prediction in pred:
        if(prediction == 1):
            #print (str(i) + ": Song: " + test["song_title"][i] + ", By: "+ test["artist"][i])
            res = {"song":test["song_title"][i],"author":test["artist"][i], "url":"https://open.spotify.com/track/"+test["id"][i]}
            arr.append(res)
            likedSongs= likedSongs + 1
        i = i +1

    print(arr)

    return JsonResponse(arr, safe = False, json_dumps_params={'ensure_ascii': False})