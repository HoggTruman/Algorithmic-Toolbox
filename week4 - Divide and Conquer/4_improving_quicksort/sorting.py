# Uses python3
import sys
import random

#elements with index up to m1-1 are less than a[l] (m1 is a less than element until the final switch)
#elements with index m1 to m2 are equal to a[l]
#elements with index m2+1 to r are greater than a[l]

def partition3(a, l, r):
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            m1 += 1
            m2 += 1
            a[i], a[m1] = a[m1], a[i]
            if m2 != m1:
                a[i], a[m2] = a[m2], a[i]

        elif a[i] == x:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
    a[l], a[m1] = a[m1], a[l]
    return m1, m2


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = l
    a[l], a[k] = a[k], a[l]
    m = partition3(a, l, r)
    randomized_quick_sort(a, l, m[0]-1);
    randomized_quick_sort(a, m[1] + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

