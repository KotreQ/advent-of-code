import sys


def main() -> None:
    start_line = sys.stdin.readline().strip()
    
    N = len(start_line)
    beam_pos = [0 for _ in range(N)]

    start_index = start_line.index("S")
    beam_pos[start_index] = 1

    timeline_count = 1

    for line in sys.stdin.readlines():
        line = line.strip()
        
        new_beam_pos = [0 for _ in range(N)]

        for i in range(N):
            if beam_pos[i] > 0:
                if line[i] == "^":
                    timeline_count += beam_pos[i]
                    new_beam_pos[i-1] += beam_pos[i]
                    new_beam_pos[i+1] += beam_pos[i]
                else:
                    new_beam_pos[i] += beam_pos[i]
    
        beam_pos = new_beam_pos

    print(timeline_count)



if __name__ == "__main__":
    main()