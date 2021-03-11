#def sum_numbers(text: str) -> int:

text = "en 1845 and 1910 year"

lst = text.split()      # split text into words
result = 0 
value=0             # sum of numbers in text
for word in lst:        # for each word
    try:                # If possible to convert word into integer,
        value = int(word)   # is mean this consist only from numbers
        print(value)
        result += value     # so add number to result.
        print(result)
    except:             # If exception has raised,
        pass            # go to next word in lst
print(lst)
print("Total:", result)
#return result
