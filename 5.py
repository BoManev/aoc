def part1():
    with open("p5", "r") as file:
        seeds = list(map(int, file.readline().split(":")[1].strip().split(" ")))
        seeds.sort()
        print(seeds)

        line = file.readline()
        while True:
            if len(file.readline()) == 0:
                break
            new_seeds = []
            while True:
                line = file.readline().strip().split(" ")
                if len(line) == 1:
                    break

                dst = int(line[0])
                src = int(line[1])
                stp = int(line[2])
                rm = []
                for i, seed in enumerate(seeds):
                    if src <= seed < src + stp:
                        new_seeds.append(dst + seed - src)
                        # pop() messes up the enumeration of seeds
                        rm.append(i)

                for i, r in enumerate(rm):
                    seeds.pop(r - i)
            seeds = new_seeds + seeds
        seeds.sort()
        print(seeds, seeds[0])
        
# number 82 -> 84 -> 84 -> 84 -> 77 -> 45 -> 46 -> 46
def part2():
    with open("p5-t", "r") as file:
        seeds = list(map(int, file.readline().strip().split(":")[1].strip().split(" ")))
        seeds = list(map(lambda seed: (seed[0], seed[0] + seed[1] - 1), zip(seeds[::2], seeds[1::2])))
        print("seeds: ", seeds, "\n")
        file.readline()
        while True:
            if len(file.readline()) == 0:
                break
            new_seeds = []
            while True:
                line = file.readline().strip().split(" ")
                if len(line) == 1:
                    break

                dst = int(line[0])
                src = int(line[1])
                stp = int(line[2])
                rm = []
                for i, (ss, se) in enumerate(seeds):
                    # SS - SR - x - x or x - x - SS - SE
                    if not(se < src or ss > src+stp):
                        # x - SS - SE - x
                        if src <= ss and src + stp >= se:
                            start = dst + (ss - src)
                            end = dst + (se - src)
                        # SS - x - SE - x
                        elif src > ss and src + stp > se:
                            start = dst
                            end = dst + (se - src)
                            new_seeds.append((ss, src))
                        # x - SS - x - SE
                        elif src < ss and src + stp < se:
                            start = dst + (ss - src)
                            end = dst + stp
                            new_seeds.append((src + stp, se))
                        # SS - x - y - SE
                        elif src > ss and se > src + stp:
                            start = dst
                            end = dst + stp
                            new_seeds.append((ss, src))
                            new_seeds.append((src + stp, se))
                        else:
                            print("LOL")
                            print(line, ss, se)
                        new_seeds.append((start, end))
                        rm.append(i)
                for i, r in enumerate(rm):
                    seeds.pop(r - i)
            
            seeds = new_seeds + seeds
        print(seeds)
        print(min(seeds, key=lambda x: x[0]))

part1()
part2()

