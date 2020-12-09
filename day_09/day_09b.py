# Network Encryption

lines = [int(l.strip("\n")) for l in open("input.txt")]

index_l = 0
index_u = 25

while True:
    preamble = lines[index_l:index_u]

    result = False
    target = lines[index_u]

    for num in preamble:
        remainder = target - num
        if remainder in preamble:
            result = True
            break

    if result:
        index_u += 1
        index_l += 1
    else:
        print(target)
        break

index_l = 0
index_u = 1

while True:
    preamble = lines[index_l:index_u]
    if sum(preamble) == target:
        print(min(preamble)+max(preamble))
        break
    elif sum(preamble) < target:
        index_u += 1
    elif sum(preamble) > target:
        index_l += 1
        index_u = index_l + 1
