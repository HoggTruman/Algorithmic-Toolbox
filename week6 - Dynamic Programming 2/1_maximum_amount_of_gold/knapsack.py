# Uses python3
import sys

def optimal_weight(W, items):
    max_weights = [[0]*(W+1) for item in (items+[0])]
    for i in range(1, len(items)+1):
        for w in range(1, W+1):
            max_weights[i][w] = max_weights[i-1][w]
            if items[i-1] <= w:
                val = max_weights[i-1][w - items[i-1]] + items[i-1]
                if max_weights[i][w] < val:
                    max_weights[i][w] = val
    return max_weights[-1][-1]



if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

