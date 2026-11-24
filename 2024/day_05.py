from collections import defaultdict
import sys


def main():
    requirements = defaultdict(set)  # page : {pages required before}

    lines = sys.stdin.readlines()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        if line == "":
            break

        a, b = map(int, line.split('|'))
        requirements[b].add(a)

    result = 0
    for line in lines[count:]:
        pages = list(map(int, line.strip().split(",")))

        n = len(pages)

        for i, page in enumerate(pages):
            required = requirements[page]
            if any(p in required for p in pages[i+1:]):
                # some following page was already required -> incorrect
                break

        else:  # not broken -> correct
            result += pages[n//2]

    print(result)


if __name__ == "__main__":
    main()