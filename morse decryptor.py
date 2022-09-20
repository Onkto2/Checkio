from ast import And


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}

code = "... --- -- .   - . -..- -"

start = 0
end = 0
spacecounter = 0
lentext = len(code)


code_temp = ""

i = 0 
while i < len(code):
    current = code[(i):(i+1)]
    if (i+1) == len(code):
        end = i+1
        code_temp = code_temp + MORSE.get(code[(start):(end)])
        print(code_temp)
        break
    else:
        try:
            if code[i].isspace():
                end = i
                code_temp = code_temp + MORSE.get(code[(start):(end)])
                start = end+1
                print(code_temp)
        except:
            code_temp = code_temp + " "
            start = end+2
            i=end+1
    i=i+1

codefinal = code_temp.capitalize()
print(codefinal)     
    
#add .capitlize() to capitalize string
