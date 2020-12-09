# Network Encryption

lines = [int(l.strip("\n")) for l in open("input.txt")]

index_l = 0
index_u = 25
invalid = 0

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
        invalid = target
        break

print(target)
