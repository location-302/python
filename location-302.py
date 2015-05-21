import hashlib
import urllib

def location302Url(id, secret, url):
	serviceUrl = "http://302-location.com"

	params = "i=" + str(id) + "&u=" + urllib.quote_plus(url)
	token = hashlib.sha256(secret + params).hexdigest()
	token = token[0:4]

	return serviceUrl + "/?" + params + "&t=" + token