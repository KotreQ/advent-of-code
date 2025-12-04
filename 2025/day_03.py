import sys


def main() -> None:
    result = 0

    for line in sys.stdin.readlines():
        line = line.strip()

        l = len(line)

        max_a = -1
        a_ind = -1
        for i in range(l-1):
            digit = int(line[i])
            if digit > max_a:
                max_a = digit
                a_ind = i
        
        max_b = -1
        for i in range(a_ind+1, l):
            digit = int(line[i])
            if digit > max_b:
                max_b = digit
        
        joltage = max_a * 10 + max_b
        result += joltage

    print(result)


if __name__ == "__main__":
    main()

