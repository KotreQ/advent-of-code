from functools import reduce
import sys

RESULT_SIZE = 12


def main() -> None:
    result = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        l = len(line)

        joltage_digits = [0 for _ in range(RESULT_SIZE)]

        last_max_index = -1
        for cur_jolt_index in range(RESULT_SIZE):
            max_digit = -1
            max_index = -1

            for i in range(last_max_index + 1, l - RESULT_SIZE + 1 + cur_jolt_index):
                digit = int(line[i])
                if digit > max_digit:
                    max_digit = digit
                    max_index = i

            last_max_index = max_index
            joltage_digits[cur_jolt_index] = max_digit

        joltage = reduce(lambda a, b: a * 10 + b, joltage_digits)
        result += joltage

    print(result)


if __name__ == "__main__":
    main()
