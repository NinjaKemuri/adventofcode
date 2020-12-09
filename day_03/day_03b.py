# Toboggan Trajectory
#
# Calculate the number of trees encountered when moving
# right 3, down 1 from the starting position
#
# Each line repeats to the right in sequence
# Coordinates are likely required to map the trees

# move = [[3, 1]]
move = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree = 1

with open("input.txt") as f:
    mountain = [[x for x in y] for y in f.read().strip().split('\n')]

    for slide in move:
        x = 1
        y = 1
        z = 0

        while (y + slide[1] - 1) <= len(mountain):
            if mountain[y - 1][(x - 1) % 31] == "#":
                z += 1

            x += slide[0]
            y += slide[1]

        tree *= z

print(tree)
