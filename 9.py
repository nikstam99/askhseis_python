print ("Δώσε αρχείο κειμένου σε ascii")
file = open(input ())
a = file.read()
x = 1
b =  [a[i:i+x] for i in range (0, len(a), x)]
c = []

for i in range (len(b)):
 c.append(b[i])
 c[i] = ord(b[i])
 c[i] = bin(c[i])[2:]
 c[i] = str(0) * (7-len(c[i])) + c[i]

d ="".join(c)
count0 = []
count1 = []
for i in range(len(d)):
 count0.append(0)
 count1.append(0)



j = 1
k = 1
for i in range(1,len(d)):
     if d[i-1]==d[i] and d[i]=='0':
          count0[j] = count0[j] + 1
     else :
           j+=1
            
     if d[i-1]==d[i] and d[i]=='1':
          count1[k] = count1[k] + 1
     else :
           j
           k+=1


print (max(count0), max(count1))
