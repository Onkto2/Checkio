# In this mission your task is to determine the popularity of certain words in the text.

# At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

# When solving this task pay attention to the following points:

# The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
# The search words are always indicated in the lowercase.
# If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
# Input: The text and the search words array.

# Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

# Precondition:
# The input text will consists of English letters in uppercase and lowercase and whitespaces.

# def popular_words(text: str, words: list) -> dict:
#     # your code here
#     return None

text = '''
When I was One
I had just begun
When I was Two
I was nearly new
'''
words = ['i', 'was', 'three', 'near']
text= text.lower()
print(text)
temp = text.split()
print(temp)

i=0
#print(temp)
dict = {}

for z in words:
    dict.update({words[i]: temp.count(z)})
    print(words[i], z.lower())
    i=i+1
    

print(dict)