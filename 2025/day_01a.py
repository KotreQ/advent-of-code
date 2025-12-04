import sys

count = 0

dial = 50
for line in sys.stdin.readlines():
    line = line.strip()

    direction = -1 if line[0] == "L" else 1
    amount = int(line[1:])

    count += amount // 100  # add the number of full rotations
    amount %= 100

    prev = dial
    dial += amount * direction

    if prev != 0 and (
        dial <= 0 or dial >= 100
    ):  # if not started at 0 and is out of bounds -> add 1 rotation
        count += 1

    dial %= 100


print(count)
