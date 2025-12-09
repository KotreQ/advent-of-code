from pprint import pprint
import sys


def compare(t1, t2):
    if t1[0] < t2[0] and t1[1] < t2[1]:
        return -1

    if t1[0] > t2[0] and t1[1] > t2[1]:
        return 1

    return 0


def area(t1, t2):
    return (abs(t2[0] - t1[0]) + 1) * (abs(t2[1] - t1[1]) + 1)


def main() -> None:
    tiles = [tuple(map(int, line.strip().split(","))) for line in sys.stdin.readlines()]

    min_tiles = set()
    max_tiles = set()

    for tile in tiles:
        min_to_remove = set()
        for min_tile in min_tiles:
            if (
                compare(tile, min_tile) == 1
            ):  # if higher than any minimal -> not a minimal
                break
            if (
                compare(tile, min_tile) == -1
            ):  # if lower than any minimal -> remove that minimal
                min_to_remove.add(min_tile)

        else:
            min_tiles.add(tile)  # not higher than any minimal -> possible minimal

        min_tiles.difference_update(min_to_remove)

        max_to_remove = set()
        for max_tile in max_tiles:
            if (
                compare(tile, max_tile) == -1
            ):  # if lower than any maximal -> not a maximal
                break
            if (
                compare(tile, max_tile) == 1
            ):  # if higher than any maximal -> remove that maximal
                max_to_remove.add(max_tile)

        else:
            max_tiles.add(tile)  # not lower than any maximal -> possible maximal

        max_tiles.difference_update(max_to_remove)

    max_area = 0
    for tile_a in min_tiles:
        for tile_b in max_tiles:
            cur_area = area(tile_a, tile_b)
            if cur_area > max_area:
                max_area = cur_area

    print(max_area)


if __name__ == "__main__":
    main()
