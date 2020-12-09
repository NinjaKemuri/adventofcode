import collections
import re


def check(bags, container, bag_colour):

    for c in bags[bag_colour]:
        container.add(c)
        check(bags, container, c)

    return container


def cost(bag_contains, bag_colour):
    total = 0
    for bag_count, inner_colour in bag_contains[bag_colour]:
        total += bag_count
        total += bag_count * cost(bag_contains, inner_colour)

    return total


def main():
    lines = [l.strip("\n") for l in open("input.txt")]

    bags = collections.defaultdict(set)
    bag_contains = collections.defaultdict(list)

    for line in lines:
        bag_colour = re.match(r'(.+?) bags contain', line)[1]
        for bag_count, inner_colour in re.findall(r'(\d+) (.+?) bags?[,.]', line):
            bag_count = int(bag_count)
            bags[inner_colour].add(bag_colour)
            bag_contains[bag_colour].append((bag_count, inner_colour))

    holds_colour = check(bags, set(), 'shiny gold')
    print(len(holds_colour))

    print(cost(bag_contains, 'shiny gold'))


if __name__ == "__main__":
    main()
