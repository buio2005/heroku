import re
import base64
import requests

web_url = 'http://speedvideo.net/embed-xg14alha5wu2-607x360.html'

f = requests.get(web_url)

html = f.text


a = re.compile('var\s+linkfile *= *"(.+?)"').findall(html)[0]
b = re.compile('var\s+linkfile *= *base64_decode\(.+?\s+(.+?)\)').findall(html)[0]
c = re.compile('var\s+%s *= *(\d*)' % b).findall(html)[0]

stream_url = a[:int(c)] + a[(int(c) + 10):]
stream_url = base64.b64decode(stream_url)

print ('URL_FIND ==>' + stream_url.decode("utf-8"))