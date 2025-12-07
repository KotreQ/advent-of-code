import sys


def main() -> None:
    start_line = sys.stdin.readline().strip()
    
    N = len(start_line)
    beam_pos = [False for _ in range(N)]

    start_index = start_line.index("S")
    beam_pos[start_index] = True

    split_count = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        
        new_beam_pos = [False for _ in range(N)]

        for i in range(N):
            if beam_pos[i]:
                if line[i] == "^":
                    split_count += 1
                    new_beam_pos[i-1] = True
                    new_beam_pos[i+1] = True
                else:
                    new_beam_pos[i] = True
    
        beam_pos = new_beam_pos

    print(split_count)



if __name__ == "__main__":
    main()