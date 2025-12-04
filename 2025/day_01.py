import sys


count = 0

dial = 50
for line in sys.stdin.readlines():
    line = line.strip()

    direction = -1 if line[0] == "L" else 1
    amount = int(line[1:])

    dial += amount * direction
    dial %= 100

    if dial == 0:
        count += 1

print(count)
