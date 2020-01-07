with open("0501.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]
mem = ROM.copy()

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
  op = mem[i]%100
  if op == 1:
    mem[mem[i + 3]] = P(1) + P(2)
    i += 4
  elif op == 2:
    mem[mem[i + 3]] = P(1) * P(2)
    i += 4
  elif op == 3:
    mem[mem[i+1]] = int(input())
    i += 2
  elif op == 4:
    print(P(1))
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

i = 0
while mem[i] != 99 and i < len(mem):
  print("Pointer: " + str(i))
  operation()
print("END")

