# Write a Python Code to Find the Term containing x^3
# in the Expansion of
# (2x − 5)^5

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = 5
a = 2
b = -5
print(f"Expansion of ({a}x {b:+})^{n} is:")

for k in range(n + 1):
    coeff = fact(n) // (fact(k) * fact(n - k))
x_part = f"x^{n - k}" if (n - k) > 1 else ("x" if (n - k) == 1 else "")
const = a ** (n - k) * (b ** k)
term_coeff = coeff * const

if term_coeff > 0 and k != 0:
    print(" + ", end="")

print(f"{term_coeff}{x_part}", end="")

print("\n")

k= 2
binom_coeff = fact(n) // (fact(k) * fact(n - k))
term = binom_coeff * (a ** (n -k)) * (b ** k)
x_power = n - k

print(f"The term containing x^{x_power} in ({a}x {b:+})^{n} is:")
print(f"{term}")
