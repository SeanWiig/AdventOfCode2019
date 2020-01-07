from collections import deque
from itertools import permutations

with open("1501.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]

p = 0
rb = 0
mem = ROM.copy()
move = 0
inputBuffer = 1
readyFlag = False
status = 0

robot = (0,0)
map = {(0,0):0}

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

def getC(d):
  if d == 1:
    return (robot[0],robot[1]-1)
  if d == 2:
    return (robot[0],robot[1]+1)
  if d == 3:
    return (robot[0]-1,robot[1])
  if d == 4:
    return (robot[0]+1,robot[1])
  else: return robot

def display():
  for y in range(25):
    for x in range(45):
      c = (robot[0]+x-22,robot[1]+y-12)
      if x == 22 and y == 12:
        print('@', end = "")
      elif c in map: 
        print(map[c], end = "")
      else:
        print(' ', end = "")
    print()

def send(mov):
  global readyFlag, inputBuffer
  readyFlag = False
  inputBuffer = mov
  while readyFlag == False:
    operation()
  return status

def probe(dir):
  

def operation():
  global p, rb, robot, move, readyFlag, status
  op = mem[p]%100
  if op == 1:
    setMem(P(3), V(1) + V(2))
    p += 4
  elif op == 2:
    setMem(P(3), V(1) * V(2))
    p += 4
  elif op == 3:
    #display()
    #move = 0
    #while move < 1 or move > 4:
    move = inputBuffer
    setMem(P(1), move)
    p += 2
  elif op == 4:
    status = V(1)
    if status == 0:
      map[getC(move)] = '#'
    if status == 1:
      map[getC(move)] = '.'
      robot = getC(move)
    if status == 2:
      map[getC(move)] = '+'
      robot = getC(move)
    readyFlag = True
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

go = True
while go:
  go = operation()