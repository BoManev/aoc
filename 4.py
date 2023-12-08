def part1():
    with open("p4", "r") as file:
        total = 0
        for i, line in enumerate(file):
            winners, attempts = line.split('|')
            winners = winners.split(":")[1].strip().replace("  ", " ").split(" ")
            attempts = attempts.strip().replace("  ", " ").split(" ")
            print(winners, attempts)
            curr = sum(int(int(winner) == int(attemp)) for winner in winners for attemp in attempts)
            if curr ==  1:
                total += 1
            elif curr > 1:
                total += 2 ** (curr - 1)
            print(curr, total)
        print(total)
    
part1()