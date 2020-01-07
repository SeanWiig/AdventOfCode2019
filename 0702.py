from collections import deque
from itertools import permutations

with open("0701.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]

p = 0
rb = 0
mem = []

def P(param):
  if param == 1:
    pMode = (mem[p]//100)%10
  elif param == 2:
    pMode = (mem[p]//1000)%10
  elif param == 3:
    pMode = (mem[p]//10000)%10
  if pMode:
    return mem[p+param]
  else:
    return mem[mem[p+param]]

def operation():
  global p
  global rb
  global mem
  
  op = mem[p]%100
  if op == 1:
    mem[mem[p + 3]] = P(1) + P(2)
    p += 4
  elif op == 2:
    mem[mem[p + 3]] = P(1) * P(2)
    p += 4
  elif op == 3:
    mem[mem[p+1]] = input()
    p += 2
  elif op == 4:
    print(P(1))
    p += 2
  elif op == 5:
    if P(1):
      p = P(2)
    else:
      p += 3
  elif op == 6:
    if P(1) == 0:
      p = P(2)
    else:
      p += 3
  elif op == 7:
    if P(1) < P(2):
      mem[mem[p+3]] = 1
    else:
      mem[mem[p+3]] = 0
    p += 4
  elif op == 8:
    if P(1) == P(2):
      mem[mem[p+3]] = 1
    else:
      mem[mem[p+3]] = 0
    p += 4
  elif op == 9:
    rb += P(1)
    p += 2
  elif op == 99:
    return False 
  return True


go = True
while go:
  go = operation()