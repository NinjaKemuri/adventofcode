def check_password(password, char, f_min, f_max):
    string_list = list(password)

    # Check both positions are not the same character
    if string_list[f_min - 1] == char and string_list[f_max - 1] == char:
        return False
    else:
        if string_list[f_min - 1] == char or string_list[f_max - 1] == char:
            return True
        else:
            return False


pass_obj = []
"""
pass_obj.append('1-3 a: abcde'.split())
pass_obj.append('1-3 b: cdefg'.split())
pass_obj.append('2-9 c: ccccccccc'.split())
print(pass_obj)

"""
with open("input.txt") as f:
    for line in f:
        pass_obj.append(line.split())

counter = 0

for item in pass_obj:
    policy_range = [int(x) for x in item[0].split('-')]
    policy_char = item[1].strip(':')
    password = item[2]

    if check_password(password, policy_char, policy_range[0], policy_range[1]):
        counter += 1

print(counter)
