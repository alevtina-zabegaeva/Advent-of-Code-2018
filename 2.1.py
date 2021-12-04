from collections import Counter


with open('input2.txt', 'r') as f:
    inpt = [Counter(line.strip()) for line in f]
# f = [
#     'abcdef',
#     'bababc',
#     'abbcde',
#     'abcccd',
#     'aabcdd',
#     'abcdee',
#     'ababab'
#     ]
# inpt = [Counter(line) for line in f]

count_2, count_3 = 0, 0
for word in inpt:
    found_2, found_3 = False, False
    for char in word:
        if word[char] == 2:
            found_2 = True
        elif word[char] == 3:
            found_3 = True
    if found_2:
        count_2 += 1
    if found_3:
        count_3 += 1

print(count_2, count_3, count_2 * count_3)
