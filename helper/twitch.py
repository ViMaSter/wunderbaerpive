from twitch import TwitchClient
import json

def printTwitchIDs():
	client = TwitchClient(client_id='hfwl010tvr2r6s4cp9xgx9um5zvftf')
	channel = client.channels.get_videos(119136051, 100, 0, 'archive')

	for val in channel:
		if(val.id[0] == 'v'):
			val.id = val.id[1:]
		print(val.id)