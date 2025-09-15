# Complete the function "digits_sum" so that it prints the sum of a three-digit number
def digits_sum(num):

  centenas = (num // 100)
  decenas = (num // 10) % 10
  unidades = (num % 10)

  return centenas + decenas + unidades


# Invoke the function with any three-digit number
print(digits_sum(123))
