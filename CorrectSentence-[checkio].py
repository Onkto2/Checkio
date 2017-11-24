def correct_sentence(text: str) -> str:
    """
        returns a corrected sentence which starts with a capital letter
        and ends with a dot.
    """
    if text[0].isupper():
        
        if text[-1] == ".":
            print("allgood")
            return text
        else:
            text = text + "."
            
            return text
        return text
    else:
        text = text[0].upper() + text[1:]
        if text[-1] == ".":
            
            return text
        else:
            text = text +"."
            return text
        return text
    return text
    

   
def correct_sentence2(text: str) -> str:
    return text.capitalize() + '.' * (not text.endswith('.'))
