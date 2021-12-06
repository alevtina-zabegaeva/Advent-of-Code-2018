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
guards_minutes = defaultdict(Counter)
length = len(inpt)
while True:
    while i < length and inpt[i][1]:
        guard_ID = inpt[i][1]
        i += 1
    if i+1 >= length:
        break
    start, end = minutes(inpt[i]), minutes(inpt[i+1])
    for j in range(start, end):
        guards_minutes[j].update([guard_ID])
    i += 2

max_sleep_time = 0
for minute, count in guards_minutes.items():
    guard = count.most_common(1)[0]
    if guard[1] > max_sleep_time:
        sleep_minute = minute
        most_sleepy_guard, max_sleep_time = guard[0], guard[1]

print(sleep_minute * most_sleepy_guard)
