


def safe_pawns(pawns):
#pawns = ({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
safe_count = 0
for p in pawns:
    #print((chr(ord(p[0])))+(chr(ord(p[1]))))
    #print(chr(ord(p[1])))
    if (chr(ord(p[0]) - 1) + chr(ord(p[1]) - 1) in pawns or
        chr(ord(p[0]) + 1) + chr(ord(p[1]) - 1) in pawns):
        safe_count += 1

#print(safe_count)
return safe_count
        
        
