items = [1,2,3,4,5];
lenlist = len(items);
list1= [];
list2=[];


    
if lenlist == 0:
    print("Empty");
elif (lenlist % 2) == 0:
    print("Even");
    for i in range (0, int(lenlist/2)):
        list1.append(items[i]);
    for j in range (int(lenlist/2), int(lenlist)):
        list2.append(items[j]);
    print(list1);
    print(list2);
else:
    for i in range (0, (int(lenlist/2)+1)):
        list1.append(items[i]);
    for j in range ((int((lenlist/2)+1)), int(lenlist)):
        list2.append(items[j]);
    print("Uneven");
    
items.clear();
items.append(list1);
items.append(list2);
print(items)