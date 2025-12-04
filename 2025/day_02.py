import sys

def is_valid(s):
    l = len(s)
    h = l // 2
    return s[:h] != s[h:]


def main() -> None:
    id_ranges = sys.stdin.readline().strip().split(",")
    
    sum_ = 0

    for id_range in id_ranges:
        start_id, end_id = map(int, id_range.split("-"))

        for id_num in range(start_id, end_id+1):
            if not is_valid(str(id_num)):
                sum_ += id_num

    print(sum_)

if __name__ == "__main__":
    main()
