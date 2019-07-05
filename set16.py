d=int(input())
if d>1:
  for i in range(2,d):
    if d%i == 0:
      print("no")
      break
  else:
      print("yes")
else:
    print("no")
