# Expand (x + 2)^4 by using the Binomial theorem in

# Python.



from unittest import result


n = 4 #exponent
a = 2 #constant value in(x + a)

def fact(num): #factorial of n
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(f"Expansion of (x + {a})^{n} is:")

for k in range(n + 1):
    # coefficient C(n,k)
    coeff = fact(n) // (fact(k) * fact(n - k))
    term_coeff = coeff * (a ** k)
    power = n - k

if power == 0:
    print(f"{term_coeff}", end="")
elif power == 1:
    print(f"{term_coeff}x +", end="")
else:
    print(f"{term_coeff}x^{power} +", end="")
