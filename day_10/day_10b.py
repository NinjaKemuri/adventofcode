lines = [int(l.strip("\n")) for l in open("input.txt")]

jolt_ones = 0
jolt_threes = 0

variations = {}


def count_vars(adapters, start, target):
    l = (len(adapters), start)

    if l in variations:
        return variations[l]

    count = 0

    if target - start <= 3:
        count += 1

    if not adapters:
        return count

    if adapters[0] - start <= 3:
        count += count_vars(adapters[1:], adapters[0], target)

    count += count_vars(adapters[1:], start, target)
    variations[l] = count

    return count


print(count_vars(sorted(lines), 0, max(lines) + 3))
