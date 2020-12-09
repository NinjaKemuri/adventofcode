# Toboggan Trajectory
#
# Calculate the number of trees encountered when moving
# right 3, down 1 from the starting position
#
# Each line repeats to the right in sequence
# Coordinates are likely required to map the trees

# Column = loop * 4 - 1 % 32
trees = 0
v_slide = 0
mountain = []

# r_step = 3
# d_step = 1

with open("input.txt") as f:
    for line in f.readlines():
        mountain.append([tile for tile in line.strip('\n')])

r_step = int(input("Enter Steps Right: "))
d_step = int(input("Enter Steps Down:  "))
for i, tiles in enumerate(mountain):
    if i % d_step == 0:
        tile = max(((v_slide * r_step) % 31) + 1, 1)
        v_slide += 1

        if tiles[tile - 1] == "#":
            trees += 1

        # print(tile, tiles[tile - 1], trees)

print(trees)
