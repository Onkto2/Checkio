def checkio(data):
    
    #all flags are false at the beginning
    upper_flag = False
    lower_flag = False
    number_flag = False
    
    #if the string is shorter than 10 characters, then the function returns false 
    if len(data) < 10:
        return False
    else:
        #if the string is longer, then the function checks for every condition to be met
        for character in data:
            if character.isupper():
                upper_flag = True
            if character.islower():
                lower_flag = True
            if character.isdigit():
                number_flag = True
        
        #then, if all flags have been marked as True in the process, then the function returns True
        return upper_flag and lower_flag and number_flag

