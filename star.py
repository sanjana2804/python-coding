def star_pattern(n):
  for i in range(n):
    print(" "*(n-i-1)+"*"*(2*n+i))
  for i in range(n - 2, -1, -1):
      print(" " * (n - i - 1) + "*" * (2 * i + 1))

n = int(input("Enter the number of rows for the diamond pattern: "))
star_pattern(n)
  
