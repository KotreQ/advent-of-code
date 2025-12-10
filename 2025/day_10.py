import re
import sys

LINE_PATTERN = re.compile(r"^\[([.#]+)\] ((?:\([\d,]+\)\s?)+) \{([\d,]+)\}$")


def get_lights_bin(schema) -> int:
    lights_bin = 0
    for char in schema[::-1]:
        lights_bin <<= 1
        if char == "#":
            lights_bin |= 1

    return lights_bin


def get_buttons_bin(buttons) -> list[int]:
    B = len(buttons)

    buttons_bin = [0 for _ in range(B)]
    for i in range(B):
        button = buttons[i]
        for light_switch in button:
            buttons_bin[i] |= 1 << light_switch

    return buttons_bin


def bitmasks(n, k):  # bitmask of k 1s in n places
    if k == 0:  # only zeroes
        yield 0
        return

    if n == k:  # only ones
        yield (1 << n) - 1
        return

    my_bit = 1 << (n - 1)

    for bitmask in bitmasks(n - 1, k - 1):
        yield my_bit | bitmask

    yield from bitmasks(n - 1, k)


def find_bitmask(target, numbers) -> int:
    N = len(numbers)

    for bit_count in range(N + 1):
        for bitmask in bitmasks(N, bit_count):
            cur_target = target
            for bit_spot in range(N):
                cur_target ^= numbers[bit_spot] * ((bitmask >> bit_spot) & 1)

            if cur_target == 0:
                return bitmask


def main() -> None:
    result = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        lights, buttons, joltages = LINE_PATTERN.match(line).groups()

        buttons = [
            tuple(map(int, button.strip("()").split(",")))
            for button in buttons.split(" ")
        ]

        lights_bin = get_lights_bin(lights)
        buttons_bin = get_buttons_bin(buttons)

        bitmask = find_bitmask(lights_bin, buttons_bin)
        result += bitmask.bit_count()

    print(result)


if __name__ == "__main__":
    main()
