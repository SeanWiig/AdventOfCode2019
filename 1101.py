from collections import deque
from itertools import permutations

with open("1101.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]

p = 0
rb = 0
mem = ROM.copy()

pos = (0,0)
heading = 0 #N=0 E=1 S=2 W=3

hull = {(0,0):1}

paintPhase = 0
paintFlag = False

def move():
  global pos
  if heading == 0:
    pos = (pos[0],pos[1]+1)
  elif heading == 1:
    pos = (pos[0]+1,pos[1])
  elif heading == 2:
    pos = (pos[0],pos[1]-1)
  elif heading == 3:
    pos = (pos[0]-1,pos[1])


def getHull(x):
  if x in hull:
    return hull[x]
  else:
    hull[x] = 0
    return 0

def paintHull(y):
  global hull
  hull[pos] = y

def P(param):
  if param == 1:
    pMode = (mem[p]//100)%10
  elif param == 2:
    pMode = (mem[p]//1000)%10
  elif param == 3:
    pMode = (mem[p]//10000)%10
  if pMode == 1:
    return p+param
  elif pMode == 2:
    return mem[p+param] + rb
  else:
    return mem[p+param]

def V(param):
  global mem
  a = P(param)
  if a >= len(mem):
    mem += [0] * (a + 1 - len(mem))
  return mem[a]

def setMem(a,d):
  global mem
  if a >= len(mem):
    mem += [0] * (a + 1 - len(mem))
  mem[a] = d

outputBuffer = 0

def operation():
  global p
  global rb
  global outputBuffer
  global paintPhase
  global paintFlag
  
  op = mem[p]%100
  if op == 1:
    setMem(P(3), V(1) + V(2))
    p += 4
  elif op == 2:
    setMem(P(3), V(1) * V(2))
    p += 4
  elif op == 3:
    setMem(P(1), getHull(pos))
    p += 2
  elif op == 4:
    #print(V(1))
    outputBuffer = V(1)
    paintPhase += 1
    paintFlag = True
    p += 2
  elif op == 5:
    if V(1):
      p = V(2)
    else:
      p += 3
  elif op == 6:
    if V(1) == 0:
      p = V(2)
    else:
      p += 3
  elif op == 7:
    if V(1) < V(2):
      setMem(P(3), 1)
    else:
      setMem(P(3), 0)
    p += 4
  elif op == 8:
    if V(1) == V(2):
      setMem(P(3), 1)
    else:
      setMem(P(3), 0)
    p += 4
  elif op == 9:
    rb += V(1)
    p += 2
  elif op == 99:
    return False 
  return True

input = 0
output = 0

go = True
while go:
  go = operation()
  if paintFlag:
    if paintPhase == 1:
      paintHull(outputBuffer)
      paintFlag = False
    elif paintPhase == 2:
      heading = (heading - 1 + (2*outputBuffer)) % 4
      move()
      paintFlag = False
      paintPhase = 0



