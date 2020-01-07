with open("0101.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content] 

def mass(m):
  return (m // 3) - 2

def this(initialMass):
  fuelReq = mass(initialMass)
  totalFuel = 0
  while fuelReq >= 0:
    print(str(totalFuel) + " + " + str(fuelReq))
    totalFuel += fuelReq
    fuelReq = mass(fuelReq)
  return totalFuel

t = 0

for x in content:
  t += this(x)
print(t)
