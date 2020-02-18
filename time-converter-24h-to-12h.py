def time_converter(time):
    
    hour = int(time[0:2])
    Minute = time[3:5]
    ampm = "am" 
    
    if hour > 12:
        hour = hour - 12
        ampm = "p.m."
    elif hour == 12:
        ampm = "p.m."
    elif hour == 0:
        hour = hour +12
        ampm = "a.m."
    else:
        ampm ="a.m."
    
    time = (str(hour)+":"+Minute+" "+ampm)
    
    return time