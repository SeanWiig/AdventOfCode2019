with open("0201.txt") as f:
    sto = f.readline().split(",")

ROM = [int(x) for x in sto]
mem = []

i = 0
f = 0
def operation(p):
  global mem
  if mem[p] == 1:
    mem[mem[p + 3]] = mem[mem[p + 2]] + mem[mem[p + 1]]
  if mem[p] == 2:
    mem[mem[p + 3]] = mem[mem[p + 2]] * mem[mem[p + 1]]

def compute(x,y):
  global mem
  mem = ROM.copy()
  mem[1] = x
  mem[2] = y
  i = 0
  while mem[i] != 99 and i < len(mem):
    operation(i)
    i += 4
  return mem[0]

for x in range(100):
  for y in range(100):
    if compute(x,y) == 19690720:
      print((x*100) + y)
  print(x)
print("END")

