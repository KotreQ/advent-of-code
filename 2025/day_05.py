import sys

def optimize_ranges(ranges):
    ranges = sorted(ranges)

    optimized = []

    last_range = ranges[0]
    for cur_range in ranges[1:]:
        if cur_range[0] > last_range[1]:
            optimized.append(last_range)
            last_range = cur_range
        
        else:
            last_range = last_range[0], max(last_range[1], cur_range[1])
    
    optimized.append(last_range)

    return optimized

def in_range(n, range_):
    return n >= range_[0] and n <= range_[1]

def main() -> None:
    ranges = []

    while True:
        line = sys.stdin.readline().strip()
        if line == "":
            break

        ranges.append(tuple(map(int, line.split("-"))))
    
    ranges = optimize_ranges(ranges)

    result = 0

    for line in sys.stdin.readlines():
        num = int(line.strip())

        for range_ in ranges:
            if in_range(num, range_):
                result += 1
                break

    print(result)


if __name__ == "__main__":
    main()