from collections import deque
from itertools import permutations

with open("0701.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]

inputBuffer = deque([])
def getInput():
  if not inputBuffer:
    return input()
  else:
    return inputBuffer.popleft()

outputBuffer = ""

def P(param):
  if param == 1:
    pMode = (mem[i]//100)%10
  if param == 2:
    pMode = (mem[i]//1000)%10
  if param == 3:
    pMode = (mem[i]//10000)%10
  if pMode:
    return mem[i+param]
  else:
    return mem[mem[i+param]]

def operation():
  global mem
  global i
  global outputBuffer
  op = mem[i]%100
  if op == 1:
    mem[mem[i + 3]] = P(1) + P(2)
    i += 4
  elif op == 2:
    mem[mem[i + 3]] = P(1) * P(2)
    i += 4
  elif op == 3:
    mem[mem[i+1]] = int(getInput())
    i += 2
  elif op == 4:
    outputBuffer = P(1)
    i += 2
  elif op == 5:
    if P(1):
      i = P(2)
    else:
      i += 3
  elif op == 6:
    if P(1) == 0:
      i = P(2)
    else:
      i += 3
  elif op == 7:
    if P(1) < P(2):
      mem[mem[i+3]] = 1
    else:
      mem[mem[i+3]] = 0
    i += 4
  elif op == 8:
    if P(1) == P(2):
      mem[mem[i+3]] = 1
    else:
      mem[mem[i+3]] = 0
    i += 4

mem = []
def getResult(phases):
  global i
  global mem
  global inputBuffer
  signal = 0
  for phase in phases:
    i = 0
    mem = ROM.copy()
    inputBuffer = deque([phase,signal])
    while mem[i] != 99 and i < len(mem):
      operation()
    signal = outputBuffer
  return signal


highscore = (0,0)
for x in list(permutations(range(0,5))):
  result = getResult(x)
  print (str(result) + ":" + str(x))
  if result > highscore[1]:
    highscore = (x,result)
print(highscore)


