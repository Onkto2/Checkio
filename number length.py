def number_length(a: int) -> int:
    numlen = len(str(a))
    return numlen

print('Example:')
print(number_length(10))

assert number_length(10) == 2
assert number_length(0) == 1
assert number_length(4) == 1
assert number_length(44) == 2

print("The mission is done! Click 'Check' to earn cool rewards!")