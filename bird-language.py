phrase = "hoooowe yyyooouuu duoooiiine"
vowels=["a","e","i","o","u","y"]
temp = ""
templetter = ""

j=0
while j < len(phrase):
    templetter = phrase[j]
    #keep double spaces from occuring
    if phrase[j].isspace():
        if phrase[j] == temp[len(temp)-1]:
            j=j+1
            continue
        else:
            temp = temp+phrase[j]
    #if letter is not a vowel add letter to temp word
    elif phrase[j] not in vowels:
        temp = temp+phrase[j]
    else:
        if phrase[j] in vowels and phrase[j-1] not in vowels and phrase[j-1].isspace() is False:
            temp = temp
            
        else:
            if phrase [j] == phrase[j+1] and phrase[j+1] == phrase[j+2]:
                temp = temp + phrase[j]
                j = j+3
                continue

    j=j+1

#phrase = temp

print(temp)