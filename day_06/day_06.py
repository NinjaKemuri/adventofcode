with open("input.txt") as f:
    result = 0

    for group in f.read().split("\n\n"):
        set_list = []
        for sets in group.split("\n"):
            set_list.append(set(sets))

        result += len(set_list[0].intersection(*set_list[1:]))

    print(result)
