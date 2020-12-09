lines = [l.rstrip('\n') for l in open("input.txt")]

acc = 0
pt = 0
seen = set()

while True:
    if pt in seen:
        print(acc)
        break

    seen.add(pt)

    line = lines[pt]
    inst, arg = line.split()
    arg = int(arg)

    if inst == "jmp":
        pt += arg
        continue

    if inst == "acc":
        acc += arg

    if inst == "nop":
        pass

    pt += 1
