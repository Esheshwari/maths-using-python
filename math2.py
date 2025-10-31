# Write a code to evaluate the number of combinations
# when choosing 2 objects out of 6 in Python.

# function to calculate factorial
from unittest import result


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 6 #total number of objects
r = 2 #number of objects to choose
combinations = fact(n) // (fact(r) * fact(n-r))
print(f"The number of combinations when choosing {r} objects out of {n} is: {combinations}")
