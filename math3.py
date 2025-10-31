# Write a Python code to Find the number of permutations
# when selecting 3 objects out of 5.

# function to calculate factorial
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5 #total number of objects
r = 3 #number of objects to choose
permutations = fact(n) // fact(n-r)
print(f"The number of permutations when choosing {r} objects out of {n} is: {permutations}")
