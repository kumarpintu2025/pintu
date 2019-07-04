def factorial(n):
  if(n==0):
    return 1
  else:
    n= n*factorial(n-1)
    return n
num=int(input())
print(factorial(num))
