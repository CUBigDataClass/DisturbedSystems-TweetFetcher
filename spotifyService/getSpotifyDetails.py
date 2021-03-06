import spotipy.oauth2 as oauth2
import requests
import json


credentials = oauth2.SpotifyClientCredentials(
        client_id="",
        client_secret="")

token = credentials.get_access_token()

url = "https://api.spotify.com/v1/search"

params = {
	"query" : "pink floyd",
	"type" : "artist",
	"limit" : 1
}

headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json",
    "Authorization": "Bearer "+token,
}
req = requests.get(url,headers=headers, params = params)

sData = req.json()
artist = {}
if "artists" in sData:
	artists = sData["artists"]["items"]
	if len(artists) != 0:
		data = artists[0]
		img1 = ""
		spotifyURL = ""
		if len(data["images"]) != 0:
			img1 = data["images"][0]
		if "spotify" in data["external_urls"]:
			spotifyURL = data["external_urls"]["spotify"]
		artist = {
			"spotifyURL" : spotifyURL,
			"spotifyPopularity" : str(data["popularity"]),
			"spotifyImage" : img1,
		}
	print (artist)
