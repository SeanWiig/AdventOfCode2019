with open("0301.txt") as f:
    content1 = f.readline().split(",")
    content2 = f.readline().split(",")
wire1 = [(x[0],int(x[1:])) for x in content1]
wire2 = [(x[0],int(x[1:])) for x in content2]

grid1 = dict()
grid2 = dict()
X = 0
Y = 0
steps1 = 0

for mov in wire1:
  if mov[0] == 'U':
    grid1.update({(X,Y+i):steps1+i for i in range(1, mov[1]+1)})
    Y += mov[1]
  elif mov[0] == 'D':
    grid1.update({(X,Y-i):steps1+i for i in range(1, mov[1]+1)})
    Y -= mov[1]
  elif mov[0] == 'R':
    grid1.update({(X+i,Y):steps1+i for i in range(1, mov[1]+1)})
    X += mov[1]
  elif mov[0] == 'L':
    grid1.update({(X-i,Y):steps1+i for i in range(1, mov[1]+1)})
    X -= mov[1]
  steps1 += mov[1]

X = 0
Y = 0
steps2 = 0
for mov in wire2:
  if mov[0] == 'U':
    grid2.update({(X,Y+i):steps2+i for i in range(1, mov[1]+1)})
    Y += mov[1]
  elif mov[0] == 'D':
    grid2.update({(X,Y-i):steps2+i for i in range(1, mov[1]+1)})
    Y -= mov[1]
  elif mov[0] == 'R':
    grid2.update({(X+i,Y):steps2+i for i in range(1, mov[1]+1)})
    X += mov[1]
  elif mov[0] == 'L':
    grid2.update({(X-i,Y):steps2+i for i in range(1, mov[1]+1)})
    X -= mov[1]
  steps2 += mov[1]

intersections = set(grid1)&set(grid2)

def dist(x):
  return grid1[x] + grid2[x]

min = 1000000000000
for x in intersections:
  c = dist(x)
  if c < min:
    min = c
    print(str(c) + " " + str(x))

#161 (-354, -401)
#89 (-639, -471)
#87 (-146, -652)
#85 (-354, -424)
