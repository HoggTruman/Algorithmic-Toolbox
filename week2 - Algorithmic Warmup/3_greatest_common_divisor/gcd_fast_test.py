import random as rd

#FAST
def gcd_fast(a, b):
    sol = [a, b]
    sol.sort(reverse=True)
    while sol[0] != 0:
        sol = [sol[1] % sol[0], sol[0]]

    return sol[1]

#NAIVE
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


# Run test
while True:
    a, b = (rd.randint(1, 2*10**5), rd.randint(1, 2*10**5))
    print(a, b)
    if gcd_naive(a, b) != gcd_fast(a, b):
        print("Uh-Oh!!!")
        break
    else:
        print("OK!!")
