from collections import defaultdict
from functools import reduce
import sys
from queue import PriorityQueue


def dist_sq(b1, b2):
    dx = b2[0] - b1[0]
    dy = b2[1] - b1[1]
    dz = b2[2] - b1[2]
    return dx**2 + dy**2 + dz**2


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])

        return self.parent[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

        return True


def main() -> None:
    boxes = []

    for line in sys.stdin.readlines():
        line = line.strip()

        boxes.append(tuple(map(int, line.split(","))))

    N = len(boxes)

    uf = UnionFind(N)
    q = PriorityQueue()
    for i in range(N - 1):
        a = boxes[i]
        for j in range(i + 1, N):
            b = boxes[j]
            q.put((dist_sq(a, b), i, j))

    last = (None, None)
    while q.qsize() > 0:
        _, u, v = q.get()

        if uf.union(u, v):
            last = (u, v)

    i, j = last
    result = boxes[i][0] * boxes[j][0]

    print(result)


if __name__ == "__main__":
    main()
