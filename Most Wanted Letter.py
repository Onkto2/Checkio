#Checkio.org Python 29/01/20 - Most Wanted Letter

text = "AAaooo!!!!"
temptext = text

maxcount = 0
maxcountletter = ""

for x in temptext:
    #print(x)
    if x.isalpha() is False:
        temptext = temptext.replace(x,"")
    if x.islower() is False:
        temptext = temptext.replace(x,x.lower())
    if x.isspace() is True:
        temptext = temptext.replace(x,"")

#print(temptext)
lentext = len(temptext)
text = temptext

i=0
while i < lentext:
    counter = temptext.count(text[i])
    if counter > maxcount:
      maxcount = counter
      maxcountletter = text[i]
    
    if counter == maxcount:

        # define an alphabet
        alfa = "abcdefghijklmnopqrstuvwxyz"

        # define reverse lookup dict
        rdict = dict([ (x[1],x[0]) for x in enumerate(alfa) ])
        if rdict[maxcountletter] > rdict[text[i]]:
            maxcountletter = text[i] 
            
    i += 1
print(maxcountletter)