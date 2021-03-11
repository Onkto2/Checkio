text='olleH Hello'
newtext = ""
i=0
j=1
x=len(text)
    
if len(text) == 0:
    for z in text.split():
        text = text.replace(z,z[::-1])    
    print(text)

while j < x:
    if text[i].isalnum() and text[j].isalnum() and j+1<x:
        j=j+1
           
            #print(text[i],text[j])
    elif text[i].isalnum() and text[j].isspace():
            y=j-1
            while y > (i-1):
                newtext = newtext+text[y]
                y=y-1
            print(newtext)
            i=j
            j=j+1
    elif j+1==x:
            print(text[i])
            print(text[j])
            y=j
            while y > i-1:
                newtext = newtext+text[y]
                y=y-1
            print(newtext)
            i=j
            j=j+1
    
    elif text[i].isspace() and text[j].isalnum():
            newtext = newtext + text[i]
            i=i+1
            j=j+1
            print("new word detected")
            print(newtext)
    
    elif text[i].isspace() and text[j].isspace():
            newtext = newtext + text[j]
            print(newtext)
            i=i+1
            j=j+1