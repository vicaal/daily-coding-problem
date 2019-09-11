

def valid_character(number):
    return True if int(number) > 0 and int(number) < 27 else False


def solve(message):
    if message == '':
        return 1
    else:
        number_of_solutions = 0
        if valid_character(message[:1]):
            number_of_solutions += (solve(message[1:]))
        if len(message) > 1 and valid_character(message[:2]):
            number_of_solutions += (solve(message[2:]))

    return number_of_solutions


assert solve('65') == 1
assert solve('23') == 2
assert solve('111') == 3
assert solve('1224') == 5
assert solve('2522') == 4
assert solve('2562') == 2
assert solve('2532') == 2
