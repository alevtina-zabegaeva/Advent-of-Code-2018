from collections import defaultdict


def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def calculate(x1, y1, x2, y2):
    points = defaultdict(set)
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            min_dist = 1000
            min_point = False
            for point in inpt:
                d = dist((i, j), point)
                if min_dist > d:
                    min_dist = d
                    min_point = point
                elif min_dist == d:
                    min_point = False
            if min_point:
                points[min_point].add((i, j))
    return points


# with open('test6.txt', 'r') as f:
with open('input6.txt', 'r') as f:
    inpt = tuple(tuple(map(int, line.strip().split(', '))) for line in f)

# print(inpt)
x_max, y_max = 0, 0
x_min, y_min = 1000, 1000
for point in inpt:
    x_max = max(x_max, point[0])
    y_max = max(y_max, point[1])
    x_min = min(x_min, point[0])
    y_min = min(y_min, point[1])
print(f'({x_min}, {y_min}) - ({x_max}, {y_max})')

points1 = calculate(x_min, y_min, x_max, y_max)
points2 = calculate(x_min-1, y_min-1, x_max+1, y_max+1)

max_len = 0
for point, s in points1.items():
    if len(s) == len(points2[point]) and max_len < len(s):
        max_len = max(max_len, len(s))

print(max_len)
