items = [4, 6, 2, 2, 6, 4, 4, 4, 6]
#items = ['bob', 'bob', 'carl', 'alex', 'bob']
#items = []
items_temp = []
switch = 0 

while len(items) > 0:
    
    for x in items:
        count = 0
        if items.count(x) > 1:
            count = items.count(x)
            #temp = items[x]
            print(count, x)
            
        i = 0
        while i < count:
            items_temp.append(x)
            items.remove(x)
            i=i+1
            continue

        if items.count(x) == 1:
            items_temp.append(0)
            items.remove(0)
            
items = items_temp

print(items_temp)
    













    
