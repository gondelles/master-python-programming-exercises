# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  left_digit = num // 10
  right_digit = num % 10
  
  # Your code here
  return int(str(right_digit) + str(left_digit))
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
