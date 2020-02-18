time = "05:55"
sunset = 60*6
sundown = 18*60

hour = time[0:2]
minute = time[3:5]
hourminute = 60*int(hour)+int(minute)
if hourminute < sunset or hourminute > sundown:
    time = "I can't see the sun!"
else:
    minutedeg = (sundown-sunset)/180 #4minutes per degree of sun rize
    deg = (hourminute-sunset)/minutedeg
    round(deg,2)
    time = deg



print(time)