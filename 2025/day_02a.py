import sys


def divisors(n: int):
    if n > 1:
        yield 1

    i = 2
    while i * i < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1

    if i * i == n:
        yield i


def check_repeating(s: str, sublen: int) -> bool:
    l = len(s)

    item = s[:sublen]

    start = sublen
    while start < l:
        if s[start : start + sublen] != item:
            return False
        start += sublen

    return True


def is_valid(s: str) -> bool:
    l = len(s)
    for sublen in divisors(l):
        if check_repeating(s, sublen):
            return False

    return True


def main() -> None:
    id_ranges = sys.stdin.readline().strip().split(",")

    sum_ = 0

    for id_range in id_ranges:
        start_id, end_id = map(int, id_range.split("-"))

        for id_num in range(start_id, end_id + 1):
            if not is_valid(str(id_num)):
                sum_ += id_num

    print(sum_)


if __name__ == "__main__":
    main()
