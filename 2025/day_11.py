import sys


def find_paths(graph, start, end, cache=None) -> int:
    if start == end:
        return 1

    if cache is None:
        cache = {}

    if start in cache:
        return cache[start]

    result = 0
    for step in graph[start]:
        paths = find_paths(graph, step, end, cache)
        result += paths

    cache[start] = result
    return result


def main() -> None:
    connections: dict[str, list[str]] = {}
    for line in sys.stdin.readlines():
        line = line.strip()
        conn_from, conns_to = line.split(":")
        conns_to = conns_to.strip().split()

        connections[conn_from] = conns_to

    print(find_paths(connections, "you", "out"))


if __name__ == "__main__":
    main()
