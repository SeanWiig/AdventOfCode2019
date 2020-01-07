with open("0601.txt") as f:
    content = f.readlines()
content = [(x[:3],x[4:7]) for x in content] 

d = {}
t = 0

for x in content:
  if x[0] in d:
    d[x[0]].append(x[1])
  else:
    d[x[0]] = [x[1]]

inv = {}

for x in content:
  inv[x[1]] = x[0]

s = {}

def bSum(c,v):
  global t
  for x in d[c]:
    t += v+1
    if x in d:
      bSum(x,v+1)

def transfer(c,v):
  if c == 'COM':
    return 0
  if inv[c] in s:
    return v + s[inv[c]]
  s[inv[c]] = v+1
  return transfer(inv[c], v+1)
