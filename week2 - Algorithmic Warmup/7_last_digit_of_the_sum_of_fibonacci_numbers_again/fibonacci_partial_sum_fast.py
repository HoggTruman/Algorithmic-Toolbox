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


def get_fibonacci_huge_fast(n, m):
    # Calculate Pisano Period
    seq = [0, 1]

    while seq == [0, 1] or seq[-1] + seq[-2] != 1:
        seq.append((seq[-1] + seq[-2]) % m)

    pisano_period = len(seq) - 1
    reqterm = n % pisano_period

    return calc_fib_faster(reqterm) % m


def fibonacci_sum_fast(n):
    return (get_fibonacci_huge_fast(n+2, 10) - 1) % 10


def fibonacci_partial_sum_fast(start, finish):
    return (fibonacci_sum_fast(finish) - fibonacci_sum_fast(start-1)) % 10


input = input()
start, finish = map(int, input.split())
print(fibonacci_partial_sum_fast(start, finish))
