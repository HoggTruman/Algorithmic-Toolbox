# Uses python3
import sys

def get_change(m):
    mincoins = [0]*4
    mincoins[0] = 1
    mincoins[1] = 2
    mincoins[2] = 1
    mincoins[3] = 1
    if m >= 5:
        mincoins += [0]*(m-4)
        for i in range(4, m):
            mincoins[i] = min(mincoins[i-1]+1, mincoins[i-3]+1, mincoins[i-4]+1)
    return mincoins[m-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
