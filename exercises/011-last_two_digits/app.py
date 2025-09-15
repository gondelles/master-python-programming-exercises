# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num:int):
    if num > 9:
        print(str(num)[-2:])
    return num

# Invoke the function with any integer greater than 9
last_two_digits(1234)
