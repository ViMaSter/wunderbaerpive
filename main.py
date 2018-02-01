import helper.twitch
import helper.youtube
import urllib.parse

from http.server import HTTPServer, BaseHTTPRequestHandler

ytHelper = helper.youtube.Helper()

class wblInterface(BaseHTTPRequestHandler):
	def step1(self, query):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(('<html><body><a href="%s">Authorize YT-access</a></body></html>' % ytHelper.generateOAuthCredentialURL()).encode('utf-8'))
	def step2(self, query):
		oAuthKey = query['code'][0]
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(b"Received key: ")
		self.wfile.write(oAuthKey.encode('utf-8'))
		self.postCallback(urllib.parse.unquote(oAuthKey))

	def do_GET(self):
		query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
		if (len(query) == 1 and 'code' in query):
			self.step2(query)
		else:
			self.step1(query)
	def do_POST(self): self.send_response(404)
	def do_PUT(self): self.send_response(404)
	def do_DELTE(self): self.send_response(404)
	@classmethod
	def run(self, requestedPort, returnCodeCallback):
		print('Listening on localhost:%s' % requestedPort)
		self.postCallback = returnCodeCallback
		server = HTTPServer(('', requestedPort), self)
		server.serve_forever()


server = wblInterface.run(1337, lambda self,x: print("Got return code: "+x))

#if __name__ == '__main__':
	# When running locally, disable OAuthlib's HTTPs verification. When
	# running in production *do not* leave this option enabled.
	# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
	# service = get_authenticated_service()
	# channels_list_by_username(service,
	#	 part='snippet,contentDetails,statistics',
	#	 forUsername='UCASywtQUrKSsd-sxrqO4SJg')