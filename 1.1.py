with open('input1.txt', 'r') as f:
    inpt = [int(line.strip()) for line in f]

print(sum(inpt))
