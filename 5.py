print ("Δώσε κείμενο σε ascii")
a = input ()
b = (a.lower())
whitelist = set('abcdefghijklmnopqrstuvwxyz αβγδεζηθικλμνξοπρστυφχψω')
bb = ''.join(filter(whitelist.__contains__, b))
c = bb.split()

from collections import Counter

C = Counter(c)
d = C.most_common(10)
print (d)

f = []
S = 0

for i in range (len(c)):
   f.append(c[i])
   e = f[i]
   f[i] = e[:2]
M = len(f)
i = 0

while M>0:
 if len(f[i])<2:
    f[i] = ''
    S = S + 1
 M = M - 1
 i = i + 1
   
from collections import Counter

Counter= Counter(f)
if S>0:
 Counter.pop('')
g = Counter.most_common(3)
print (g)
j = []

for i in range (len(c)):
   j.append(c[i])
   h = j[i]
   j[i] = h[:3]
M = len(j)
i = 0

while M>0:
 if len(j[i])<3:
    j[i] = ''
    S = S + 1
 M = M - 1
 i = i + 1
 
from collections import Counter

Counter = Counter(j)
if S>0:
 Counter.pop('')
k = Counter.most_common(3)
print (k)
 

