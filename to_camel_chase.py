def to_camel_case(name: str) -> str:
    i=0
    tempname = ""
    while i < len(name):
        
        if name[i] == "_":
            tempname = tempname + name[(i+1)].capitalize()
            i=i+2
        tempname = tempname + name[i]
        i=i+1
    tempname1 = tempname.replace(tempname[0],tempname[0].capitalize(),1)
    name=tempname1
    # replace this for solution
    return name



print("Example:")
print(to_camel_case("my_function_name"))

assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")