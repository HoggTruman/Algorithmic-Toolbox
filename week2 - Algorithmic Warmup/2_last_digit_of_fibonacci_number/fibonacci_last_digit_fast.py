def get_fibonacci_last_digit_fast(n):
    if n == 0:
        return 0
    seqlist = [0] * (n + 1)
    seqlist[1] = 1
    for i in range(2, n + 1):
        seqlist[i] = (seqlist[i-1] + seqlist[i-2]) % 10

    return seqlist[n]


n = int(input())
print(get_fibonacci_last_digit_fast(n))
