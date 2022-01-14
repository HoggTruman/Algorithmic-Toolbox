# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def return_end(elem):
    return elem.end


def optimal_points(segments):
    points = []
    sol = []
    segments.sort(key=return_end)
    for s in segments:
        points.append(s.start)
        points.append(s.end)

    for segment in segments:
        point_needed = True
        for point in sol:
            if segment.start <= point <= segment.end:
                point_needed = False
                break
        if point_needed:
            sol.append(segment.end)

    return sol

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    #print(segments)
    points = optimal_points(segments)
    print(len(points))
    print(*points)



# STRATEGY:
# find the a point which intersects the most and then remove those segments??
#need to sort by start point??