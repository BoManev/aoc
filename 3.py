from math import prod


def part1():
    with open("p3", "r") as file:
        total = 0
        lines = list(map(str.strip, file.readlines()))
        lines_count = len(lines)
        for i, line in enumerate(lines):
            line_sz = len(line)
            j = 0
            while j < line_sz:
                c = line[j]
                if c.isdigit():
                    for dj, d in enumerate(line[j:]):
                        if not d.isdigit():
                            num = int(line[j : j + dj])  # [j, dj)
                            end = j + dj - 1  # line[end] <- index of last digit
                            break
                        elif j + dj == line_sz - 1:
                            num = int(line[j : j + dj + 1])  # [j, dj]
                            end = j + dj
                            break
                    for x in range(max(i - 1, 0), min(i + 2, lines_count)):
                        for y in range(max(j - 1, 0), min(end + 2, line_sz)):
                            if not lines[x][y].isdigit() and lines[x][y] != ".":
                                total += num
                                break
                    j = end + 1
                    continue
                j += 1
        print(total)


def part2():
    with open("p3", "r") as file:
        total = 0
        lines = list(map(str.strip, file.readlines()))
        lines_count = len(lines)
        for i, line in enumerate(lines):
            line_sz = len(line)
            for j, c in enumerate(line):
                if c == "*":
                    hits = []
                    for x in range(max(i - 1, 0), min(i + 2, lines_count)):
                        for y in range(max(j - 1, 0), min(j + 2, line_sz)):
                            if lines[x][y].isdigit():
                                hits.append((x, y))
                    nums = []
                    while len(hits) > 0:
                        cx, cy = hits.pop(0)
                        hit = lines[cx][cy]
                        if hit.isdigit():
                            starti = cy
                            endi = 0
                            while starti >= 0:
                                curr = lines[cx][starti]
                                line_sz = len(lines[cx])

                                if not curr.isdigit() or starti == 0:
                                    if not curr.isdigit():
                                        start = starti + 1
                                    elif starti == 0:
                                        start = starti
                                    else:
                                        raise NotImplementedError("unreachable")
                                    endi = cy + 1
                                    while endi < line_sz:
                                        curr = lines[cx][endi]
                                        if not curr.isdigit() or endi == line_sz - 1:
                                            if not curr.isdigit():
                                                end = endi
                                            elif endi == line_sz - 1:
                                                end = endi + 1
                                            else:
                                                raise NotImplementedError("unreachable")

                                            num = int(lines[cx][start:end])
                                            nums.append(num)
                                            break
                                        else:
                                            if (cx, endi) in hits:
                                                hits.remove((cx, endi))
                                        endi += 1
                                    break
                                else:
                                    if (cx, starti) in hits:
                                        hits.remove((cx, starti))
                                starti -= 1
                    if len(nums) == 2:
                        total += prod(nums)
        print(total)


part1()
part2()
