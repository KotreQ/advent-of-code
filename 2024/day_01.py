import sys


def main() -> None:
    list_a = []
    list_b = []

    for line in sys.stdin.readlines():
        line = line.strip()
        a, b = map(int, line.split())
        list_a.append(a)
        list_b.append(b)

    list_a.sort()
    list_b.sort()

    result = 0
    for a, b in zip(list_a, list_b):
        result += abs(a - b)

    print(result)


if __name__ == "__main__":
    main()
