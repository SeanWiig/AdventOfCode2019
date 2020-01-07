from collections import deque
from itertools import permutations

with open("0901.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]

p = 0
rb = 0
mem = ROM.copy()

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


def operation():
  global p
  global rb
  
  op = mem[p]%100
  if op == 1:
    setMem(P(3), V(1) + V(2))
    p += 4
  elif op == 2:
    setMem(P(3), V(1) * V(2))
    p += 4
  elif op == 3:
    setMem(P(1), int(input()))
    p += 2
  elif op == 4:
    print(V(1))
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