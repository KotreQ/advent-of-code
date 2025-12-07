import sys


def main() -> None:
    input_sheet = []
    result = 0

    for line in sys.stdin.readlines():
        line = line.strip("\n")
        input_sheet.append(line)

    WIDTH = len(input_sheet[0])
    NUMBER_ROWS = len(input_sheet) - 1

    equations = [[]]

    for col in range(WIDTH):
        number = ""
        for row in range(NUMBER_ROWS):
            if input_sheet[row][col] != " ":
                number += input_sheet[row][col]

        if number == "":
            equations.append([])
        else:
            equations[-1].append(int(number))

    equation_types = input_sheet[-1].strip().split()

    for i in range(len(equations)):
        if equation_types[i] == "+":
            value = 0
            for num in equations[i]:
                value += num

        else:
            value = 1
            for num in equations[i]:
                value *= num
        
        result += value

    print(result)


if __name__ == "__main__":
    main()
