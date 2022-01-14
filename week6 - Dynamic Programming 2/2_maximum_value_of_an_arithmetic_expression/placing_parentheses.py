import math as m


def minmax(i, j, min_mat, max_mat, dataset):
    minimum = m.inf
    maximum = -m.inf
    for k in range(i, j):
        maxmax = eval(max_mat[i][k]+dataset[2*k+1]+max_mat[k+1][j])
        minmin = eval(min_mat[i][k]+dataset[2*k+1]+min_mat[k+1][j])
        maxmin = eval(max_mat[i][k]+dataset[2*k+1]+min_mat[k+1][j])
        minmax = eval(min_mat[i][k]+dataset[2*k+1]+max_mat[k+1][j])
        minimum = min(minimum, maxmax, minmin, maxmin, minmax)
        maximum = max(maximum, maxmax, minmin, maxmin, minmax)

    return str(minimum), str(maximum)


def get_maximum_value(dataset):
    num_operators = len(dataset) // 2
    num_digits = num_operators + 1
    min_mat = [[0] * num_digits for digit in range(num_digits)]
    max_mat = [[0] * num_digits for digit in range(num_digits)]

    # initialise matrix
    for i in range(num_digits):
        min_mat[i][i] = dataset[2*i]
        max_mat[i][i] = dataset[2*i]

    # fill rest of matrices
    for s in range(1, num_digits):
        for i in range(num_digits - s):
            j = s + i
            min_mat[i][j], max_mat[i][j] = minmax(i, j, min_mat, max_mat, dataset)

    return max_mat[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
