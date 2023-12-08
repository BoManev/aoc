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


part1()
