def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here   

    dia1 = (hr1 * 3600) + (min1*60) + sec1
    dia2 = (hr2 * 3600) + (min2*60) + sec2

    return dia2 - dia1


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
