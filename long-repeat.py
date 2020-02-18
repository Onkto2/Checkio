line = "aa"

counter = 0
l1=0
l2=1

if len(line) == 0:
    counter = 0
    print("Largest repeating occuring: ", counter)
elif len(line) == 1:
    counter = 1
    print("Largest repeating occuring: ", counter)
elif len(line) == 2:
    counter = 2
    print("Largest repeating occuring: ", counter)
else:

    while l2 <= len(line):
        if l2+1 >= len(line):
            break
        else:


            while line[l1] == line[l2]:

                if l2+1 >= len(line):
                    break
                else:
                    l2=l2+1
                    if counter < (l2-l1):
                        counter = (l2-l1)
        l1=l2
        
        l2=l2+1
   
    


    