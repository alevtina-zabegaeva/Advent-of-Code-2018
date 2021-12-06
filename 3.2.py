import re


# with open('test3.txt', 'r') as f:
with open('input3.txt', 'r') as f:
    inpt = [list(map(int, re.split(r'[# @,:x]+', line.strip())[1:])) for line in f]

claims = {}
claims2 = set(range(1, len(inpt) + 1))  # all IDs

for rec in inpt:
    for i in range(rec[3]):
        for j in range(rec[4]):
            point = (rec[1] + i, rec[2] + j)
            if point in claims:
                claims2.discard(rec[0])
                claims2.discard(claims[point])
            else:
                claims[point] = rec[0]

print(claims2)
