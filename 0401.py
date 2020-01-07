def check(x):
  for i in range(6):
    dig[i] = x%10
    x //= 10
  flag = 0
  success = False
  for i in range(5):
    if dig[i] < dig[i+1]:
      return False
    if dig[i] == dig[i+1]:
      flag += 1
    else:
      if flag == 1:
        success = True
      flag = 0
  return success or (flag==1)


t = 0
dig = [0] * 6
for x in range(353096,843212):
  if check(x):
    t+=1
    print(x)

#274