import re
import sys


def main():
    PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    result = 0
    for line in sys.stdin.readlines():
        for match in PATTERN.finditer(line):
            x = int(match.group(1))        
            y = int(match.group(2))        
            result += x * y

    print(result)
    

if __name__ == "__main__":
    main()