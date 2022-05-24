

from datetime import date, timedelta

a = (2014, 12, 31) # 31 december 2014
b = (2011, 1, 1) # 1 january 2011

#def days_diff(a, b):
t1 = date(*a);
t2 = date(*b);

if t2 > t1:
    intDays = int((t2-t1).days);
else:
    intDays = int((t1-t2).days);
print((t1-t2).days);
print(intDays);
    # your code here
#    return None
