import math as m
import random

def minimum_distance_naive(points):
    num_points = len(points)
    mindist = -1
    for i in range(num_points):
        for j in range(i+1, num_points):
            dist = m.sqrt((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2)
            if dist < mindist or mindist == -1:
                mindist = dist
    return mindist

def minimum_distance_fast(points):
    n = len(points)
    points.sort(key=lambda x: x[0])
    if n//2 > 1:
        d1 = minimum_distance_fast(points[:n//2])
        d2 = minimum_distance_fast(points[n//2:])
        d = min(d1, d2)

        midline = (points[n//2 - 1][0] + points[n//2][0]) / 2
        new_points =[]
        for i in range(n):
            if midline - points[i][0] <= d:
                new_points.append(points[i])

        new_points.sort(key=lambda x: x[1])
        dprime = -1
        l = len(new_points)
        for i in range(l):
            for j in range(i + 1, l):
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



###########################################
while True:
    p = random.randint(1, 5)
    points = [0] * p
    for i in range(p):
        points[i] = [random.randint(-15, 15), random.randint(-15, 15)]

    sol1 = minimum_distance_naive(points)
    sol2 = minimum_distance_fast(points)

    print("points:", points)
    print([sol1, sol2])

    if sol1 != sol2:
        print("WRONG!!")
        break
    else:
        print("OK")


# [[-8, -15], [-2, 6], [4, 9], [11, -6], [14, -15]] (WRONG)