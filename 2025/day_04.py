import sys


def get_adj(row, col, height, width):
    for y in range(row - 1, row + 2):
        for x in range(col - 1, col + 2):
            if 0 <= y < height and 0 <= x < width and (y != row or x != col):
                yield y, x


def main() -> None:
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    result = 0

    adj_counts = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] != "@":
                continue

            for adj_row, adj_col in get_adj(row, col, HEIGHT, WIDTH):
                adj_counts[adj_row][adj_col] += 1

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if grid[row][col] == "@" and adj_counts[row][col] < 4:
                result += 1

    print(result)


if __name__ == "__main__":
    main()
