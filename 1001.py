import math

with open("1001.txt") as f:
    sto = f.readlines()

X = len(sto[0])-1
Y = len(sto)

asteroids = set()
for l in range(Y):
  for c in range(X):
    if sto[l][c] == '#':
      asteroids.add((c,l))

astdict = {(x[0],x[1]):0 for x in asteroids}

def vSub(a,b):
  return (a[0] - b[0],a[1] - b[1])

def vAdd(a,b):
  return (a[0] + b[0],a[1] + b[1])

def vDiv(a,d):
  return (a[0]//d,a[1]//d)

highscore = (0,0)
for a in astdict:
  score = 0
  for b in astdict:
    if b != a:
      v = vSub(b,a)
      gcd = math.gcd(v[0],v[1])
      v = vDiv(v,gcd)
      cursor = vAdd(a,v)
      while not cursor in astdict:
        cursor = vAdd(cursor,v)
      if cursor == b:
        score += 1
  astdict[a] = score
  if score > highscore[1]:
    highscore = (a,score)





#if X and Y have a common divisor, 

20,30

2,3