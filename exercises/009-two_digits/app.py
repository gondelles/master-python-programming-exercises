# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  # Your code here
  left_digit = number // 10
  right_digit = number % 10

  return left_digit, right_digit
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
