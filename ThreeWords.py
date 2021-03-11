''' Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). 
The words contains only letters. You should check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string with words.
Output: The answer as a boolean.
Precondition: 
The input contains words and/or numbers. 
There are no mixed words (letters and digits combined).
0 < len(words) < 100 '''

#def checkio(words: str) -> bool:

words = "Hello World 123 hello"
temp = words.split()
x=len(temp)
counter = 0
solution = bool(False)

i=0

while i < x:
    answer=temp[i].isalpha()
    if answer is True:
        counter += 1
        if counter >= 3:
            solution = True
    else:
        counter = 0
    print(answer)
    i=i+1

print(solution)
#return solution()

