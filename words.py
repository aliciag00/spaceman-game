words = []
with open('words.txt', 'r') as file:
    for line in file:
        arr = line.split(' ')
        for word in arr:
            words.append(word.strip())
