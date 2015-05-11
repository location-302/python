import hashlib
import urllib

def location302Url(id, secret, url):
	serviceUrl = "http://302-location.com"
	redirectUrl = urllib.quote_plus(url)

	params = "id=" + str(id) + "&url=" + redirectUrl
	token = hashlib.sha256(secret + params).hexdigest()

	return serviceUrl + "/?" + params + "&token=" + token