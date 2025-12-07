import sys


def main() -> None:
    start_line = sys.stdin.readline().strip()
    
    N = len(start_line)
    beam_poss = [False for _ in range(N)]
    
    start_index = start_line.index("S")
    beam_poss[start_index] = True

    split_count = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        
        for i in range(N):
            if line[i] == "^" and beam_poss[i]:
                split_count += 1
                beam_poss[i] = False
                beam_poss[i-1] = True
                beam_poss[i+1] = True
    
    print(split_count)



if __name__ == "__main__":
    main()