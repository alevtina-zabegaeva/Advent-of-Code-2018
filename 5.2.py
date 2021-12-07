def check_pair(char1, char2):
    return char1.lower() == char2.lower() and char1 != char2


# with open('test5.txt', 'r') as f:
with open('input5.txt', 'r') as f:
    inpt = f.read()
letters = set(inpt.lower())
inpt = list(inpt)

min_len = len(inpt)
for letter in letters:
    inpt_wo_letter = list(filter(lambda a: a != letter and a != letter.upper(), inpt))
    old_len = len(inpt_wo_letter) + 1
    while len(inpt_wo_letter) < old_len:
        old_len = len(inpt_wo_letter)
        i = 0
        while i+1 < len(inpt_wo_letter):
            if check_pair(inpt_wo_letter[i], inpt_wo_letter[i+1]):
                inpt_wo_letter.pop(i)
                inpt_wo_letter.pop(i)
                i = max(0, i-1)
            else:
                i += 1
    min_len = min(min_len, old_len)

print(min_len)
