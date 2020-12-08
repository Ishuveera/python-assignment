filename = "count.txt"

lines = 0
words = 0
chars = 0

with open(filename, 'r') as f:
    for line in f:
        word = line.split()

        lines += 1
        words += len(word)
        chars += len(line)
print(lines)
print(words)
print(chars)
