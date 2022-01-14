# Uses python3
import sys
import math as m

def optimal_sequence(n):
    num_moves = [[0]]*(n+1)
    for i in range(2, n+1):
        iter_vec = [m.inf, m.inf, m.inf]
        iter_vec[0] = num_moves[i-1][0] + 1
        if i % 2 == 0:
            iter_vec[1] = num_moves[i//2][0] + 1
        if i % 3 == 0:
            iter_vec[2] = num_moves[i//3][0] + 1

        min_moves = min(iter_vec)
        num_moves[i] = [min_moves, iter_vec.index(min_moves)]

    # work backwards
    x = n
    moves_vec = [n]
    while x != 1:
        if num_moves[x][1] == 0:
            x -= 1
        elif num_moves[x][1] == 1:
            x //= 2
        else:
            x //= 3
        moves_vec.append(x)

    return [num_moves[n][0], reversed(moves_vec)]


# print result
input = sys.stdin.read()
n = int(input)
sol = optimal_sequence(n)
print(sol[0])
for x in sol[1]:
    print(x, end=" ")
