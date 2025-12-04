import sys


def stream_diffs(nums):
    nums = iter(nums)

    prev = next(nums)
    for new in nums:
        yield new - prev
        prev = new


def sign(n):
    if n > 0:
        return 1
    if n < 0:
        return -1
    return 0


def main() -> None:
    result = 0

    for report in sys.stdin.readlines():
        report = list(map(int, report.strip().split()))

        prev_sign = 0
        for diff in stream_diffs(report):
            cur_sign = sign(diff)
            if cur_sign == 0:
                break

            if cur_sign == -prev_sign:
                break

            if abs(diff) > 3:
                break

            prev_sign = cur_sign

        else:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
