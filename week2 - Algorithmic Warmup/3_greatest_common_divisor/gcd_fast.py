def gcd_fast(a, b):
    sol = [a, b]
    sol.sort(reverse=True)
    while sol[0] != 0:
        sol = [sol[1] % sol[0], sol[0]]

    return sol[1]


input = input()
a, b = map(int, input.split())
print(gcd_fast(a, b))
