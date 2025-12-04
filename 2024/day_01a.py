from collections import defaultdict
import sys


def main() -> None:
    list_a = []
    b_counts = defaultdict(int)

    for line in sys.stdin.readlines():
        line = line.strip()
        a, b = map(int, line.split())
        list_a.append(a)
        b_counts[b] += 1
    
    result = 0

    for a in list_a:
        result += a * b_counts[a]
        
    print(result)



if __name__ == "__main__":
    main()
