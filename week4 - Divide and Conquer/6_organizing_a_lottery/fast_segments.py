import math as ma
import sys

def bs_greater_equal(sequence, point):
    low = 0
    high = len(sequence) - 1

    while low <= high:
        pivot = ma.floor((low+high)/2)
        pivotval = sequence[pivot]
        if pivotval >= point:
            if pivot != 0 and sequence[pivot-1] >= point:
                high = pivot - 1
            else:
                return pivot
        else:
            low = pivot + 1


def bs_less_equal(sequence, point):
    final = len(sequence) - 1
    low = 0
    high = final

    while low <= high:
        pivot = ma.floor((low+high)/2)
        pivotval = sequence[pivot]
        if pivotval <= point:
            if pivot != final and sequence[pivot+1] <= point:
                low = pivot + 1
            else:
                return pivot
        else:
            high = pivot - 1


def fast_count_segments_new(starts,ends,points):
    n = len(starts)
    starts.sort()
    ends.sort()
    count = [0] * len(points)
    for p in range(len(points)):
        l = bs_less_equal(starts, points[p])
        r = bs_greater_equal(ends, points[p])
        if l is None or r is None:
            continue

        count[p] = l - r + 1
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    cnt = fast_count_segments_new(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

