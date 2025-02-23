n=int(input("Enter the number of terms you need :"))
n1=0
n2=1
if n<=0:
  if n<0:
    print("the number of terms is negative")
  else:
    print(n2)
else:
  print("Fibonacci sequence : ", n1,n2,end=" ")
  for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")
