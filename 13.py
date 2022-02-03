from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
import json
a = json.loads(data.decode('utf-8'))
r = a['randomness']
c = str(r)
d = [(c)[i:i+2] for i in range (0, len(c), 2)]
from urllib.request import Request, urlopen

req = Request('http://api.opap.gr/draws/v3.0/1100/last-result-and-active', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
e = urlopen(req).read()
import json
f = json.loads(e.decode('utf-8'))
g = f['last']
h = g['winningNumbers']
k = h['list']
m = 0

for i in range (len(d)):
 d[i] = int(d[i],16)
 d[i] = int(d[i])
 d[i] = d[i]%80

d = set(d)
d = list(d)
         
for i in range (len(d)):
 for j in range (len(k)):
  if d[i] == k[j]:
      m = m + 1
   
print (m)
