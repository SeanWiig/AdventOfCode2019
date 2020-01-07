with open("1401.txt") as f:
    sto = f.readlines()

recipes = {}

for r in sto:
  l = r.split(" ")
  ilist = []
  for i in range((len(l) - 3) // 2):
    if l[i*2+1][-1] == ',':
      l[i*2+1] = l[i*2+1][:-1]
    ilist.append([int(l[i*2]),l[i*2+1]])
  recipes[l[-1][:-1]] = [int(l[-2]),0,ilist]

totalOre = 1000000000000
totalFuel = 0

def satisfy(s,n):
  if n <= recipes[s][1]:
    return
  global totalOre
  num = 1 + ((n - 1 - recipes[s][1]) // recipes[s][0])
  for r in recipes[s][2]:
    if r[1] == "ORE":
      totalOre -= num * r[0]
      if totalOre < 0:
        print(totalFuel)
    else:
      satisfy(r[1],r[0]*num)
      recipes[r[1]][1] -= r[0]*num
  recipes[s][1] += num*recipes[s][0] 

#while totalOre >= 0:
#  satisfy("FUEL", totalFuel + 1)
#  totalFuel += 1