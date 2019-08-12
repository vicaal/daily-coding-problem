def solve(list_numbers, k):
    number_summed_equals_k = set()
    for number in list_numbers:
        if number in number_summed_equals_k:
            return True
        number_summed_equals_k.add(k-number)
    return False


assert solve([10, 15, 3, 7], 17)
assert not solve([10, 15, 3], 17)