with open('input1.txt', 'r') as f:
    inpt = [int(line.strip()) for line in f]

summ = 0
frequency = {summ}
found = False

while not found:
    for i in inpt:
        summ += i
        if summ not in frequency:
            frequency.add(summ)
        else:
            print('found!')
            found = True
            break

print(summ)
