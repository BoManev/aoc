from functools import reduce
import sys
from math import prod


def part1():
    with open("p2", "r") as file:
        sum = 0
        for i, line in enumerate(file):
            colors = {"red": 12, "green": 13, "blue": 14}
            items = list(
                map(
                    lambda item: item.strip().split(" "),
                    reduce(
                        lambda group, acc: group + acc,
                        map(
                            lambda group: group.split(";"),
                            line.strip().split(":")[1].split(","),
                        ),
                        [],
                    ),
                )
            )
            sum += i + 1
            for count, item in items:
                current = colors.get(item, None)
                if int(count) > current:
                    sum -= i + 1
                    break
        print(sum)


def part2():
    with open("p2", "r") as file:
        total = 0
        for line in file:
            items = list(
                map(
                    lambda item: item.strip().split(" "),
                    reduce(
                        lambda item, acc: acc + item,
                        map(
                            lambda item: item.split(";"),
                            line.strip().split(":")[1].split(","),
                        ),
                        [],
                    ),
                )
            )
            colors = {"red": 0, "green": 0, "blue": 0}
            for count, item in items:
                current = colors.get(item, None)
                if current < int(count):
                    colors[item] = int(count)
            total += prod(colors.values())

        print(total)


part1()
part2()
