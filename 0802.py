with open("0801.txt") as f:
    sto = f.readline()

w = 25
h = 6

ptr = len(sto) - 2
layer = [['E' for i in range(w)] for j in range(h)]
while ptr != -1:
  for c in [(x,y) for y in range(h) for x in range(w)]:
    if sto[ptr] == '1':
      layer[c[1]][c[0]] = ' '
    elif sto[ptr] == '0':
      layer[c[1]][c[0]] = 'X'
    ptr -= 1

layer2 = [['E' for i in range(w)] for j in range(h)]

for c in range(w * h):
  ptr = c
  while sto[ptr] == '2':
    ptr += w*h
  if sto[ptr] == '1':
    layer2[c//w][c%w] = ' '
  if sto[ptr] == '0':
    layer2[c//w][c%w] = 'X'
  print(sto[ptr])

def printl(x):
  for l in x:
    print(''.join(l))