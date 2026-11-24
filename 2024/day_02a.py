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


def check_safety(diffs):
    prev_sign = 0
    for diff in diffs:
        cur_sign = sign(diff)
        if cur_sign == 0:
            break

        if cur_sign == -prev_sign:
            break

        if abs(diff) > 3:
            break

        prev_sign = cur_sign

    else:
        return True
    return False



def main() -> None:
    result = 0

    for report in sys.stdin.readlines():
        report = list(map(int, report.strip().split()))

        n = len(report)

        if check_safety(stream_diffs(report)):
            result += 1
        else:
            for skip in range(n):
                diffs = stream_diffs(report[:skip] + report[skip+1:])
                if check_safety(diffs):
                    result += 1
                    break

    print(result)


if __name__ == "__main__":
    main()
