from collections import defaultdict, Counter


def minutes(rec):
    return int(rec[0][-2:])


# with open('test4.txt', 'r') as f:
with open('input4.txt', 'r') as f:
    inpt = []
    for line in f:
        date, guard = line.strip()[1:].split('] ')
        if '#' in guard:
            guard = int(guard[7:].split()[0])
        else:
            guard = False
        inpt.append((date, guard))

inpt.sort()
# for rec in inpt:
#     print(rec)
i = 0
guards_summ = defaultdict(int)
guards_minutes = defaultdict(Counter)
guard_ID = 0
length = len(inpt)
while True:
    while i < length and inpt[i][1]:
        guard_ID = inpt[i][1]
        i += 1
    if i+1 >= length:
        break
    start, end = minutes(inpt[i]), minutes(inpt[i+1])
    guards_summ[guard_ID] += end - start
    guards_minutes[guard_ID].update(range(start, end))
    i += 2

guards_summ = dict(sorted(guards_summ.items(), key=lambda item: item[1]))
most_sleepy_guard = guards_summ.popitem()[0]
print(most_sleepy_guard * guards_minutes[most_sleepy_guard].most_common(1)[0][0])
