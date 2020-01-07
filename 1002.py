import math

def vSub(a,b):
  return (a[0] - b[0],a[1] - b[1])

def vAdd(a,b):
  return (a[0] + b[0],a[1] + b[1])

def vDiv(a,d):
  return (a[0]//d,a[1]//d)

with open("1001.txt") as f:
    sto = f.readlines()

A = (11,11)
X = len(sto[0])-1
Y = len(sto)

asteroids = set()
astdict = {}
for l in range(Y):
  for c in range(X):
    if sto[l][c] == '#' and not (l == 11 and c == 11):
      asteroids.add((c,l))

for x in asteroids:
  v = vSub(x,A)
  if v[0] < 0:
    astdict[x] = math.atan2(v[0],-v[1]) + 2*math.pi
  else:
    astdict[x] = math.atan2(v[0],-v[1])

asteroids = set()
mylist = sorted(astdict.items(), key = lambda kv:kv[1])
print(len(astdict))

num = 0

while num < 300:
  mylist = sorted(astdict.items(), key = lambda kv:kv[1])
  for b in mylist:
    v = vSub(b[0],A)
    gcd = math.gcd(v[0],v[1])
    if gcd == 0:
      continue
    v = vDiv(v,gcd)
    cursor = vAdd(A,v)
    while not cursor in astdict:
      cursor = vAdd(cursor,v)
    if cursor == b[0]:
      num += 1
      asteroids.add(cursor)
      print(str(num) + ": " + str(b[0]))
  for key in asteroids:
    astdict.pop(key, None)
  asteroids = set()
