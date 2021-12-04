with open('input2.txt', 'r') as f:
    inpt = [line.strip() for line in f]
# inpt = [
#     'abcde',
#     'fghij',
#     'klmno',
#     'pqrst',
#     'fguij',
#     'axcye',
#     'wvxyz'
#     ]

found = False
for i in range(len(inpt) - 1):
    for j in range(i + 1, len(inpt)):
        if inpt[i] == inpt[j]:
            continue
        for k in range(len(inpt[i])):
            word1 = inpt[i][:k] + inpt[i][k+1:]
            word2 = inpt[j][:k] + inpt[j][k+1:]
            if word1 == word2:
                print(word2)
                found = True
                break
        if found:
            break
    if found:
        break
