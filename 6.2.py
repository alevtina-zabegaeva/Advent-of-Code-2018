def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def calculate(x1, y1, x2, y2, l):
    points = []
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum_len = 0
            for point in inpt:
                sum_len += dist((i, j), point)
            if sum_len < l:
                points.append((i, j))
    return len(points)


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

size = 10000

area = calculate(x_min, y_min, x_max, y_max, size)
print(area)
