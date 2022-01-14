def calc_fib_faster(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fiblist = [0, 1]

    for i in range(2, n+1):
        fiblist.reverse()
        fiblist[1] = sum(fiblist)

    return fiblist[1]


n = int(input())
print(calc_fib_faster(n))
