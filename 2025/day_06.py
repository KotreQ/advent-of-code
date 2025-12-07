import sys


def main() -> None:
    equations = []

    result = 0

    for line in sys.stdin.readlines():
        line = line.strip()
        line = line.split()

        if line[0].isdecimal():    
            line = list(map(int, line))

            for i in range(len(equations), len(line)):
                equations.append([0, 1])
            
            for i in range(len(line)):
                equations[i][0] += line[i]
                equations[i][1] *= line[i]
                
        else: # finishing loop
            for i in range(len(line)):
                eq_type = line[i]

                if eq_type == "+":
                    result += equations[i][0]
                elif eq_type == "*":
                    result += equations[i][1]

    print(result)

if __name__ == "__main__":
    main()