def attempt_fix(prog):
    acc = 0
    pt = 0
    seen = set()

    while True:
        if pt == len(prog):
            return acc

        if pt in seen:
            return None

        seen.add(pt)

        line = prog[pt]
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


lines = [l.rstrip('\n') for l in open("input.txt")]

for index in range(len(lines)):
    prog = lines[:]
    if prog[index].startswith('jmp'):
        prog[index] = prog[index].replace('jmp', 'nop')
    elif prog[index].startswith('nop'):
        prog[index] = prog[index].replace('nop', 'jmp')

    x = attempt_fix(prog)
    if x:
        print(x)
