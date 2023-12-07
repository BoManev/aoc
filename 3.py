def part1():
    with open("p3", "r") as file:
        total = 0
        lines = list(map(str.strip, file.readlines()))
        lines_count = len(lines)
        for i, line in enumerate(lines):
            line = line.strip()
            line_sz = len(line)
            j = 0
            while j < line_sz:
                c = line[j]
                if c.isdigit():
                    for dj, d in enumerate(line[j:]):
                        if not d.isdigit():
                            num = int(line[j:j+dj])
                            end = j + dj - 1
                            break
                        elif j + dj == line_sz - 1:
                            num = int(line[j:j + dj + 1])
                            end = j + dj
                            break
                    for x in range(max(i-1, 0), min(i + 2, lines_count)):
                        for y in range(max(j-1,0), min(end + 2, line_sz)):
                            if (not lines[x][y].isdigit() and lines[x][y] != '.'):
                                total += num
                                break
                    j = end + 1
                    continue
                j += 1
        print(total)

part1()