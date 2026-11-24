from collections import defaultdict
import sys


def sort_pages(pages: list, requirements: dict[int: set]):
    pages_set = frozenset(pages)
    requirements = {
        page: requirements[page] & pages_set
        for page in pages_set
    }

    result = []

    visited = {page: False for page in pages}

    def dfs(u):
        if visited[u]:
            return
        visited[u] = True

        for v in requirements[u]:
            dfs(v)
        result.append(u)

    for page in pages:
        dfs(page)

    return result


def main():
    requirements = defaultdict(set)  # page : {pages required before}

    lines = sys.stdin.readlines()

    count = 0
    for line in lines:
        count += 1
        line = line.strip()
        if line == "":
            break

        a, b = map(int, line.split('|'))
        requirements[b].add(a)

    result = 0
    for line in lines[count:]:
        pages = list(map(int, line.strip().split(",")))

        n = len(pages)

        for i, page in enumerate(pages):
            required = requirements[page]
            if any(p in required for p in pages[i+1:]):
                # some following page was already required -> incorrect
                sorted_pages = sort_pages(pages, requirements)
                result += sorted_pages[n//2]
                break

    print(result)


if __name__ == "__main__":
    main()