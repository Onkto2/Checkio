def from_camel_case(name: str) -> str:
    tempname = ""
    i=0
    while i < len(name):
        if name[i].isupper() and i==0:
            tempname = tempname + name[i].lower()
        elif name[i].isupper():
            tempname = tempname + "_" + name[i].lower()
        else:
            tempname = tempname + name[i]     
        i=i+1     
            
    name = tempname
    return name


print("Example:")
print(from_camel_case("MyFunctionName"))

assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")