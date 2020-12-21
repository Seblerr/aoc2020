def byCount(minCount, maxCount, char, password):
    return minCount <= password.count(char) <= maxCount

def byIndex(a, b, char, password):
    return (password[a-1] == char or password[b-1] == char) and (password[a-1] != password[b-1])

with open('dataset') as f:
    p1Counter = 0
    p2Counter = 0
    for line in f:
        splitline = line.split(":")
        policy = splitline[0].split()
        char = policy[1]
        a, b = policy[0].split("-")
        a, b = int(a), int(b)
        password = splitline[1].strip()

        # Part one
        if byCount(a, b, char, password):
            p1Counter += 1

        # Part two
        if byIndex(a, b, char, password):
            p2Counter += 1

    print("Part one", p1Counter)
    print("Part two", p2Counter)
