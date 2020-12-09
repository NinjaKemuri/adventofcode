infile = open('advent_2020_03_input.txt','r')

field = []
for x in infile:
    field.append(x.rstrip())

def slope(n, m):
    x, y, t = 0, 0, 0
    w, c = len(field[0]), len(field)
    for i in range(0, c, n):
        t, x, y = t+['.', '#'].index(field[x][y]), x+n, y+m
        y = y-w if y >= w else y
    return t

print("Part 1: " + str(slope(1,3)))
print("Part 2: " + str(slope(1,1)*slope(1,3)*slope(1,5)*slope(1,7)*slope(2,1)))
