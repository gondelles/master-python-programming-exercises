def apple_sharing(n,k):
  # Your code here
  x = k // n

  total = k % x

  return x, total
 

print(apple_sharing(6,50))
