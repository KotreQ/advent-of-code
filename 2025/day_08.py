from collections import defaultdict
from functools import reduce
from pprint import pprint
import sys


def dist_sq(b1, b2):
    dx = b2[0] - b1[0]
    dy = b2[1] - b1[1]
    dz = b2[2] - b1[2]
    return dx**2 + dy**2 + dz**2


def find_graph_index(graphs, element):
    for i, graph in enumerate(graphs):
        if element in graph:
            return i

    return -1


def main() -> None:
    CONNECTION_COUNT = 1000
    boxes = []

    for line in sys.stdin.readlines():
        line = line.strip()

        boxes.append(tuple(map(int, line.split(","))))

    N = len(boxes)

    connections = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            connections.append((dist_sq(boxes[i], boxes[j]), i, j))
    connections.sort()

    edges = [(v1, v2) for _, v1, v2 in connections[:CONNECTION_COUNT]]
    graphs = [set([v]) for v in range(N)]

    for v1, v2 in edges:
        g1 = find_graph_index(graphs, v1)
        g2 = find_graph_index(graphs, v2)

        if g1 != g2:
            graphs[g1].update(graphs.pop(g2))

    sizes = [len(graph) for graph in graphs]
    sizes.sort(reverse=True)

    product = reduce(lambda a, b: a * b, sizes[:3])
    print(product)

if __name__ == "__main__":
    main()
