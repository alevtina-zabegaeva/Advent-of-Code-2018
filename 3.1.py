import re


# with open('test3.txt', 'r') as f:
with open('input3.txt', 'r') as f:
    inpt = [list(map(int, re.split(r'[# @,:x]+', line.strip())[1:])) for line in f]

print(inpt)
claims = set()
claims2 = set()

for rec in inpt:
    for i in range(rec[3]):
        for j in range(rec[4]):
            point = (rec[1] + i, rec[2] + j)
            if point in claims:
                claims2.add(point)
            else:
                claims.add(point)

print(claims2)
print(len(claims2))
