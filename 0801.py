with open("0801.txt") as f:
    sto = f.readline()

w = 25
h = 6

ptr = 0
lowscore = [0,150]

while sto[ptr] != '\n':
  score = 0
  for x in range(w * h):
    ptr += 1
    if sto[ptr] == '0':
      score += 1
  if score <= lowscore[1]:
    lowscore[0] = ptr - w*h
    lowscore[1] = score
    print(str(ptr) + ":" + str(score))

ptr = lowscore[0]

score0 = 0
score1 = 0
score2 = 0
for x in range(w * h):
  if sto[ptr+x] == '0':
      score0 += 1
  if sto[ptr+x] == '1':
      score1 += 1
  if sto[ptr+x] == '2':
      score2 += 1
