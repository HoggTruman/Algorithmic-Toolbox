#Uses python3
import sys
import math as m

def minimum_distance_naive(x, y):
    num_points = len(x)
    mindist = -1
    for i in range(num_points):
        for j in range(i+1, num_points):
            dist = m.sqrt((x[j]-x[i])**2 + (y[j]-y[i])**2)
            if dist < mindist or mindist == -1:
                mindist = dist
    return mindist


def minimum_distance_fast(points):
    n = len(points)
    if n//2 > 1:
        d1 = minimum_distance_fast(points[:n//2])
        d2 = minimum_distance_fast(points[n//2:])
        d = min(d1, d2)

        midline = (points[n//2 - 1][0] + points[n//2][0]) / 2
        new_points = []
        for i in range(n):
            if midline - points[i][0] <= d:
                new_points.append(points[i])

        new_points.sort(key=lambda x: x[1])
        dprime = -1
        l = len(new_points)
        for i in range(l):
            for j in range(i + 1, min(i + 8, l)):
                dist = m.sqrt((new_points[j][0] - new_points[i][0]) ** 2 + (new_points[j][1] - new_points[i][1]) ** 2)
                if dist < dprime or dprime == -1:
                    dprime = dist
        return min(d, dprime)


    else:
        d = -1
        for i in range(n):
            for j in range(i + 1, n):
                dist = m.sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
                if dist < d or d == -1:
                    d = dist
        return d




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = [(x[i], y[i]) for i in range(len(x))]
    points.sort(key=lambda x: x[0])
    print("{0:.9f}".format(minimum_distance_fast(points)))
