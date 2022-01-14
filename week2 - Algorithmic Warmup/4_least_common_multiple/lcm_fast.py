def gcd_fast(a, b):
    sol = [a, b]
    sol.sort(reverse=True)
    while sol[0] != 0:
        sol = [sol[1] % sol[0], sol[0]]
    return sol[1]


def lcm_fast(a, b):
    return int(a*b/gcd_fast(a, b))


input = input()
a, b = map(int, input.split())
print(lcm_fast(a, b))

