from datetime import datetime, date, time, timezone
import re

time = "09.07.1995 16:01";
temp = re.split(',|:| ', time);
date = temp[0].split('.');
lendate = len(date);
temp.pop(0);

i = 0
while i < len(date):
    temp.insert(i,date[i])
    i=i+1

q=0
while q < len(temp):
    if temp[q][0:1] == "0":
        temp[q] = temp[q][1:2]
        print(temp[q]);
    q=q+1

x = datetime(int(temp[2]), int(temp[1]), int(temp[0]))

xtime = datetime(int(temp[2]), int(temp[1]), int(temp[0]), int(temp[3]), int(temp[4]))

print(xtime.year)
print(xtime.strftime("%A"))

strhour = " hours "
strminutes = " minutes"

if temp[3] == "1":
    strhour = " hour "
    
if temp[4] == "1":
    strminutes = " minute"

readtime = temp[0] + " " + xtime.strftime("%B") + " " + xtime.strftime("%Y") + " " + "year" + " " + temp[3] + strhour + temp[4] + strminutes

time = readtime;

print(time);


datetimedict = {
    "day": 2,
    "month": 21,
    "year": 2022,
    "hours": 0o2,
    "minutes": 0o2
    }
    
j=0    
for key in datetimedict:
    datetimedict.update({key:temp[j]})
    j=j+1
    
 