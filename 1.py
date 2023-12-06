def part1():
    with open("p1", "r") as file:
        sum = 0
        for line in file:
            line = line.strip()
            first = next(filter(str.isdigit, line), None)
            last = next(filter(str.isdigit, reversed(line)), None)
            sum += int(first + last)

        print(sum)


def part2():
    with open("p1", "r") as file:
        sum = 0
        for line in file:
            digits = []
            for i, c in enumerate(line):
                if c.isdigit():
                    digits.append(c)
                for j, val in enumerate(
                    [
                        "one",
                        "two",
                        "three",
                        "four",
                        "five",
                        "six",
                        "seven",
                        "eight",
                        "nine",
                    ]
                ):
                    if line[i:].startswith(val):
                        digits.append(str(j + 1))
            sum += int(digits[0] + digits[-1])

        print(sum)


part1()
part2()
