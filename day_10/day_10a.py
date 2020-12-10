lines = [int(l.strip("\n")) for l in open("input.txt")]

lines.append(0)
lines.append(max(lines) + 3)
lines.sort()

jolt_ones = 0
jolt_threes = 0

for x, y in zip(lines, lines[1:]):
    if y - x == 1:
        jolt_ones += 1
    elif y - x == 3:
        jolt_threes += 1

print(jolt_ones * jolt_threes)
