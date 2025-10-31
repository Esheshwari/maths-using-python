# Write a Python function fact(n) that calculates the factorial of
# n using a loop.

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Test the function
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {fact(num)}")
