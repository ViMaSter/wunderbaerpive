import json

import os
import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

class Helper:
	def __init__(self):
		clientSecretsFile = json.load(open('client_id.json'))
		self.client_id = clientSecretsFile['installed']['client_id']

	def generateOAuthCredentialURL(self):
		scope = 'https://www.googleapis.com/auth/youtube.force-ssl'
		return ('https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=%s&redirect_uri=http://127.0.0.1:1337&scope=%s&prompt=consent&access_type=offline' %
			(self.client_id,
			 scope))

class API:
	def __init__(self, oAuthCredentials):
		APISeviceName = 'youtube'
		APIVersion = 'v3'
		self.service = build(APISeviceName, APIVersion, credentials = oAuthCredentials)

	def channels_list_by_username(self, service, **kwargs):
		results = service.channels().list(
			**kwargs
		).execute()
	
		print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
		 (results['items'][0]['id'],
			results['items'][0]['snippet']['title'],
			results['items'][0]['statistics']['viewCount']))