# Complete the function to return the respective number of the century
import math

def century(year):

  if year  <= 0:
    raise ValueError("Debe ser un numero positivo")

  return math.ceil(year / 100)


# Invoke the function with any given year
print(century(1850))
