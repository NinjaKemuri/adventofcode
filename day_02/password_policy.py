def check_password(password, char, f_min, f_max):
    # Check occurrences of character in password
    if f_min <= list(password).count(char) <= f_max:
        return True

    return False


pass_obj = []
with open("input.txt") as f:
    for line in f:
        print(line.split())
        pass_obj.append(line.split())

counter = 0
for item in pass_obj:
    # print(item)
    policy_range = [int(x) for x in item[0].split('-')]
    # print(policy_range)
    policy_char = item[1].strip(':')
    password = item[2]

    if check_password(password, policy_char, policy_range[0], policy_range[1]):
        counter += 1

print(counter)
