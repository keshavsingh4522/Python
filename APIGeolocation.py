import urllib.parse , urllib.error , urllib.request
import json
import ssl
s=0
serviceurl='http://py4e-data.dr-chuck.net/json?'


address=input('Enter location :')
url= serviceurl + urllib.parse.urlencode({'address':address,'key' : 42})
print('Retrieving',url)
data=urllib.request.urlopen(url).read().decode()
print('Retrieved :',len(data),' characters')
try:
    info=json.loads(data)
except:
    info=None
if not info or 'status' not in info or info['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
print('Place Id ',info["results"][0]["place_id"])
