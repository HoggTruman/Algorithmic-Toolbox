# Uses python3

def diff(x, y):
    if x == y:
        return 0
    else:
        return 1


def edit_distance(s, t):
    # Create path matrix
    numrows = len(t)+1
    numcols = len(s)+1
    path_mat = [[0]*numcols for row in range(numrows)]

    #initialise default values
    for i in range(numrows):
        path_mat[i][0] = i
    for j in range(numcols):
        path_mat[0][j] = j

    for i in range(1, numrows):
        for j in range(1, numcols):
            path_mat[i][j] = min(path_mat[i][j-1]+1, path_mat[i-1][j]+1, path_mat[i-1][j-1] + diff(s[j-1], t[i-1]))


    return path_mat[-1][-1]

