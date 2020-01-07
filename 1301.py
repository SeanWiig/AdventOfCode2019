from collections import deque
from itertools import permutations

with open("1301.txt") as f:
    sto = f.readline().split(",")

screen = {}
wbuf = [0,0]
write = 0

ROM = [int(x) for x in sto]

p = 0
rb = 0
mem = ROM.copy()

paddle = 0
ball = 0

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
  global p,rb, write, ball, paddle
  
  op = mem[p]%100
  if op == 1:
    setMem(P(3), V(1) + V(2))
    p += 4
  elif op == 2:
    setMem(P(3), V(1) * V(2))
    p += 4
  elif op == 3:
    printScreen()
    move = ball - paddle
    if move > 0:
      move = 1
    if move < 0:
      move = -1
    input()
    print("Ball = {} Paddle = {} Move = {}".format(ball,paddle,move))
    setMem(P(1), move)
    p += 2
  elif op == 4:
    if write == 2:
      if V(1) == 3:
        paddle = wbuf[0]
      elif V(1) == 4:
        ball = wbuf[0]
      screen[(wbuf[0],wbuf[1])] = V(1)
    else:
      wbuf[write] = V(1)
    write = (write + 1) % 3
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

blocks = [' ','#','=','_','O']

def printScreen():
  if (-1,0) in screen:
    print(screen[(-1,0)])
  for y in range(24):
    for x in range(45):
      print(blocks[screen[(x,y)]], end = "")
    print()

def play():
  global mem
  mem = ROM.copy()
  go = True
  while go:
    go = operation()

play()