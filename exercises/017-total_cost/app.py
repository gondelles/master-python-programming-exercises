# Complete the function to return the total cost in dollars and cents of (n) cupcakes
def total_cost(d, c, n):

    centavos = (d * 100) + c

    total = centavos * n

    total_usd = total // 100

    total_cent = total % 100

    return (total_usd,total_cent)


# Invoke the function with three integers: total_cost(dollars, cents, number_of_cupcakes)
print(total_cost(15,22,4))
