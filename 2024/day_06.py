from enum import Enum
import sys


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def right(self):
        return self.__class__((self.value + 1) % 4)

    def vector(self):
        match self:
            case self.UP:
                return (-1, 0)
            case self.DOWN:
                return (1, 0)
            case self.LEFT:
                return (0, -1)
            case self.RIGHT:
                return (0, 1)


def main():
    obstacles = set()
    guard = [(None, None), None]

    taken_path = set()

    lines = list(line.strip() for line in sys.stdin.readlines())
    height = len(lines)
    width = len(lines[0])

    for i, line in enumerate(lines):
        line = line.strip()
        for j, c in enumerate(line):
            match c:
                case '#':
                    obstacles.add((i, j))
                case '^':
                    guard = [(i, j), Direction.UP]

    while 0 <= guard[0][0] < height and 0 <= guard[0][1] < width:
        y, x = guard[0]

        taken_path.add((y, x))

        dy, dx = guard[1].vector()
        ny = y + dy
        nx = x + dx

        if (ny, nx) in obstacles:
            guard[1] = guard[1].right()
        else:
            guard[0] = (ny, nx)

    print(len(taken_path))


if __name__ == "__main__":
    main()