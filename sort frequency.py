items = [4,6,2,2,2,6,4,4,4]
item_temp = []
frequency = {}

# iterating over the list
for item in items:
   # checking the element in dictionary
   if item in frequency:
      # incrementing the counr
      frequency[item] += 1
   else:
      # initializing the count
      frequency[item] = 1

# printing the frequency
print(frequency)

#sort the frequency
from collections import OrderedDict
sorted = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
print(sorted)


for key, value in sorted.items():
    item_temp.extend([key] * int(value))
    
       

print(item_temp)
    
