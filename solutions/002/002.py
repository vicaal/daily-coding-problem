from operator import mul
from functools import reduce


def solve_using_division(list_numbers):
    product = reduce(mul, list_numbers)
    new_list = list()

    for number in list_numbers:
        new_list.append(product/number)

    return new_list

def solve_without_using_division(list_numbers):
    new_list = list()
    temp_list = list()
    for number in list_numbers:
        temp_list.extend(list_numbers)
        temp_list.remove(number)
        new_list.append(reduce(mul, temp_list))
        del temp_list[:]
    
    return new_list


assert solve_using_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solve_using_division([3, 2, 1]) == [2, 3, 6]
assert not solve_using_division([3, 2, 1]) == [2, 3, 7]

assert solve_without_using_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solve_without_using_division([3, 2, 1]) == [2, 3, 6]
assert not solve_without_using_division([3, 2, 1]) == [2, 3, 7]
