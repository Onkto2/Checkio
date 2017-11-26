def second_index(text: str, symbol: str):
    """
        returns the second index of a symbol in a given text
    """

    str1 = text;
    str2 = symbol;
    index2=0

    var = (str1.find(str2))
    print(var)
    if var == -1:
        index2 = None
        
    else:
        index2 = (str1.find(str2, var+1))
        if index 2 == -1:
            index2 = None


     
    return index2
