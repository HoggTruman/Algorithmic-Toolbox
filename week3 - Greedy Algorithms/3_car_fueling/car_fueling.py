# python3
import sys

def compute_min_refills(distance, tank, stops):
    num_stops = 0
    road = [0]*(len(stops)+2)
    for i in range(len(stops)): road[i+1] = stops[i]
    road[-1] = distance
    i = 0

    while True:
        if road[-1] - road[i] <= tank:
            return num_stops
        if road[i+1] - road[i] > tank:
            return -1

        j = i
        while road[j+1] - road[i] <= tank and j+1 <= len(road)-1:         #updating i too soon??
            j += 1
        i = j
        num_stops += 1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
