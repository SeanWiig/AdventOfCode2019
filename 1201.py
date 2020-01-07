from copy import deepcopy
with open("1201.txt") as f:
    sto = f.readlines()

mpos = [[0 for i in range(3)] for j in range(4)]
mvel = [[0 for i in range(3)] for j in range(4)]

for i in range(len(sto)):
  mpos[i][0] = int(sto[i].split("=")[1].split(",")[0])
  mpos[i][1] = int(sto[i].split("=")[2].split(",")[0])
  mpos[i][2] = int(sto[i].split("=")[3].split(">")[0])


mpinit = deepcopy(mpos)
mvinit = deepcopy(mvel)

def applyvel():
  for i in range(4):
    for d in range(3):
      mpos[i][d] += mvel[i][d]

def applygrav():
  for i in range(4):
    for j in range(4):
      for d in range(3):
        if mpos[i][d] < mpos[j][d]:
          mvel[i][d] += 1
        elif mpos[i][d] > mpos[j][d]:
          mvel[i][d] -= 1

def getE():
  tot = 0
  for i in range(len(mpos)):
    pot = 0
    kin = 0
    for j in range(3):
      pot += abs(mpos[i][j])
      kin += abs(mvel[i][j])
    print(pot*kin)
    tot += pot * kin
  return tot
  
i = 1
applygrav()
applyvel()
while (mpos != mpinit) or (mvel != mvinit):
  applygrav()
  applyvel()
  i += 1