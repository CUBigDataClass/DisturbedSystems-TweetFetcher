import spotipy.oauth2 as oauth2
import requests
import json


credentials = oauth2.SpotifyClientCredentials(
        client_id="e5dc70c1a984472f888c93032327a9f5",
        client_secret="22c2782e5e7f45c6898dcb8bb34a4ee0")

token = credentials.get_access_token()

url = "https://api.spotify.com/v1/search"

params = {
	"query" : "adventures of rain dance maggie",
	"type" : "track",
	"limit" : 1
}

headers = {
	"Accept" : "application/json",
	"Content-Type": "application/json",
    "Authorization": "Bearer "+token,
}
req = requests.get(url,headers=headers, params = params)

sData = req.json()
# print sData
track = {}
if "tracks" in sData:
	tracks = sData["tracks"]["items"]
	if len(tracks) != 0:
		data = tracks[0]
		tid = data["id"]
		eid = data["external_ids"]
		if "isrc" in eid:
			eid = data["external_ids"]["isrc"]
		else:
			eid = "N/A"
		duration = data["duration_ms"]
		popularity = data["popularity"]
		fullName = data["name"]

		artistList = data["artists"]

		album = data["album"]
		albumName = album["name"]
		albumRelease = album["release_date"]
		aid = album["id"]
		albumArt = ""
		spotifyURL = ""
		if len(album["images"]) != 0:
			albumArt = album["images"][0]["url"]
		if "spotify" in album["external_urls"]:
			spotifyURL = album["external_urls"]["spotify"]


		track = {
			"trackID" : tid,
			"isrc" : eid,
			"duration" : duration,
			"popularity" : popularity,
			"fullName" : fullName,
			"albumImage" : albumArt,
			"albumURL" : spotifyURL,
			"albumID" : aid
		}
		print track