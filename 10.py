print ("Δώσε αρχείο κειμένου σε ascii")
file = open(input ())
a = file.read()
x = 1
b =  [a[i:i+x] for i in range (0, len(a), x)]
c = []
d = []
e = []

for i in range (len(b)):
 c.append(b[i])
 d.append(0)
 e.append(0)
 c[i] = ord(b[i])
 c[i] = bin(c[i])[2:]
 c[i] = str(0) * (7-len(c[i])) + c[i]
 d[i] = c[i][:2]
 e[i] = c[i][5:]

 f = []
for i in range (len(c)):
 f.append(0)
 f[i] = d[i]+ e[i]

g = []
j = 0
 
if len(f)%4 == 0:
 h = len(f) // 4
 for i in range (h):
  g.append(0)
  g[i] = f[j] + f[j+1] + f[j+2] + f[j+3]
  j = j + 4

else:
 h = len(f) // 4 + 1
 for i in range (h):
  if j<= len(f)-4:
   g.append(0)
   g[i] = f[j] + f[j+1] + f[j+2] + f[j+3]
   j = j + 4
  else:
   j = len(f)

p_z = 0
p_3 = 0
p_5 = 0
p_7 = 0

for i in range (len(g)):
 g[i] = int(g[i])
 if g[i]%2 == 0:
     p_z = p_z + 1
 if g[i]%3 == 0:
     p_3 = p_3 + 1
 if g[i]%5 == 0:
     p_5 = p_5 + 1
 if g[i]%7 == 0:
     p_7 = p_7 + 1

pos_z = p_z/len(g)*100
pos_3 = p_3/len(g)*100
pos_5 = p_5/len(g)*100
pos_7 = p_7/len(g)*100

print (pos_z,'%')
print (pos_3,'%')
print (pos_5,'%')
print (pos_7,'%')

