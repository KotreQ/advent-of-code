import re
import sys


def main():
    PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do(n't)?\(\)")

    result = 0
    do = True
    for line in sys.stdin.readlines():
        for match in PATTERN.finditer(line):
            if match.group(0).startswith("mul(") and do:
                x = int(match.group(1))
                y = int(match.group(2))
                result += x * y

            elif match.group(0).startswith("do("):
                do = True

            elif match.group(0).startswith("don't("):
                do = False

    print(result)
    

if __name__ == "__main__":
    main()