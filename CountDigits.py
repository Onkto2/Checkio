''' You need to count the number of digits in a given string.
Input: A Str.
Output: An Int. '''

#def count_digits(text: str) -> int:
text = "en 1845 and 1910 year"
result = 0

for karakter in text:
    try:
        value = int(karakter)
        result = result+1
    except:
        pass
print(result)


#return 0