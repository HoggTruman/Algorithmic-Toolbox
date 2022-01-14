#Uses python3
import sys

def diff(x, y):
    if x == y:
        return 1
    else:
        return 0


def lcs2(a, b):
    # Create path matrix
    numrows = len(a) + 1
    numcols = len(b) + 1
    path_mat = [[0] * numcols for row in range(numrows)]


    for i in range(1, numrows):
        for j in range(1, numcols):
            path_mat[i][j] = max(path_mat[i][j - 1], path_mat[i - 1][j], path_mat[i - 1][j - 1] + diff(a[i - 1], b[j - 1]))
    return path_mat[-1][-1] #min(len(a),len(b),


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))


