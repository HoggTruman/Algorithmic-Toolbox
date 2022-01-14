import sys

def slow_count(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i+1:])):
            if a[i] > a[i+j+1]:
                count += 1
    return count


def merge(b, c):
    num_inversions = 0
    new_a = [0]*(len(b)+len(c))
    i = 0
    j = 0
    k = 0
    max_b_index = len(b) - 1
    max_c_index = len(c) - 1
    while i <= max_b_index and j <= max_c_index:
        if b[i] > c[j]:
            num_inversions += len(b[i:])
            new_a[k] = c[j]
            j += 1
            k += 1
        else:
            new_a[k] = b[i]
            i += 1
            k += 1
    # dump rest
    if i > max_b_index:
        new_a[k:] = c[j:]
    else:
        new_a[k:] = b[i:]

    return [new_a, num_inversions]


def merge_inversions(a):
    num_inversions = 0
    if len(a) == 1:
        return [a, num_inversions]
    piv = len(a) // 2
    b = merge_inversions(a[:piv])
    c = merge_inversions(a[piv:])
    new_a = merge(b[0], c[0])
    num_inversions += b[1]+c[1]+new_a[1]
    return [new_a[0], num_inversions]


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_inversions(a)[1])




