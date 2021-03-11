''' You are given an array of integers. 
You should find the sum of the integers with even indexes (0th, 2nd, 4th...). 
Then multiply this summed number and the final element of the array together. 
Don't forget that the first element has an index of 0.
For an empty array, the result will always be 0 (zero). '''

''' Preconditions:
0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array) '''

def checkio(array: list) -> int:
if len(array) == 0:
    return 0
else:
    multi = array[-1]
    Temp = array[::2]
    print(Temp)
    sumtemp = sum(Temp)*multi
    print(sumtemp)
return sumtemp