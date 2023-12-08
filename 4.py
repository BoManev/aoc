def part1():
    with open("p4", "r") as file:
        total = 0
        for i, line in enumerate(file):
            winners, attempts = line.split("|")
            winners = winners.split(":")[1].strip().replace("  ", " ").split(" ")
            attempts = attempts.strip().replace("  ", " ").split(" ")
            curr = sum(
                int(int(winner) == int(attemp))
                for winner in winners
                for attemp in attempts
            )
            if curr == 1:
                total += 1
            elif curr > 1:
                total += 2 ** (curr - 1)
        print(total)


def part2():
    with open("p4", "r") as file:
        m = {}
        for i, line in enumerate(file):
            winners, attempts = line.split("|")
            winners = winners.split(":")[1].strip().replace("  ", " ").split(" ")
            attempts = attempts.strip().replace("  ", " ").split(" ")
            matches = sum(
                int(int(winner) == int(attemp))
                for winner in winners
                for attemp in attempts
            )
            if not m.get(i, None):
                m[i] = 1
            if matches != 0:
                rr = list(range(i + 1, i + matches + 1))
                copies = m.get(i, None)
                for r in rr:
                    current = m.get(r, None)
                    if not current:
                        m[r] = copies + 1
                    else:
                        m[r] = current + copies
        total = sum(m.values())
        print(total)


part1()
part2()
