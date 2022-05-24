items = [4, 4, 4, 4, 6, 6, 2, 2];

items_temp = []
switch = 0 
    
while len(items) > 0:
    count = 0
    for x in items:
        if items.count(x) > 1:
            count = items.count(x)
            #temp = items[x]
            print(count)
        else:
            switch = 1
    if switch == 1: 
        i = 0
        while i < count:
            items_temp.append(x)
            items.remove(x)
            i=i+1
        else:
            items_temp.append(items[0])
            items.remove(items[0])
    
items = items_temp;
    
print(items);