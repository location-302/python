import hashlib
import urllib

def location302Url(id, secret, url):
	serviceUrl = "http://302-location.com"

	id = str(id)
	token = hashlib.sha256(secret+id+url).hexdigest()
	token = token[0:4]

	params = "i=" + id + "&u=" + urllib.quote_plus(url) + "&t=" + token
	return serviceUrl + "/?" + params