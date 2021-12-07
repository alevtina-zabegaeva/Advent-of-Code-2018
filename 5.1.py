def check_pair(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2


# with open('test5.txt', 'r') as f:
with open('input5.txt', 'r') as f:
    inpt = list(f.read())

# print(inpt)
old_len = len(inpt) + 1
while len(inpt) < old_len:
    old_len = len(inpt)
    i = 0
    while i+1 < len(inpt):
        if check_pair(inpt[i], inpt[i+1]):
            inpt.pop(i)
            inpt.pop(i)
            i = max(0, i-1)
        else:
            i += 1

print(old_len)
