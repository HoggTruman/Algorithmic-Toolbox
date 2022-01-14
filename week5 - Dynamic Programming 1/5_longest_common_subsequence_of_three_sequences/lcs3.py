# Uses python3

import sys


def diff(x, y, z):
    if x == y == z:
        return 1
    else:
        return 0


def lcs3(a, b, c):
    seqs = [a, b, c]
    seqs.sort(key=len)
    a = seqs[0]
    b = seqs[1]
    c = seqs[2]
    # Create path matrix
    numx = len(a) + 1
    numy = len(b) + 1
    numz = len(c) + 1
    path_mat = [[[0] * numx for y in range(numy)] for z in range(numz)]

    for i in range(1, numx):
        for j in range(1, numy):
            for k in range(1, numz):
                path_mat[k][j][i] = max(path_mat[k][j][i - 1], path_mat[k][j - 1][i], path_mat[k - 1][j][i],
                                        path_mat[k - 1][j - 1][i - 1] + diff(a[i - 1], b[j - 1], c[k - 1]))
    return path_mat[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))


