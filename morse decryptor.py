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

code_temp = ""

i = 0 
while i < len(code):
    if code[i].isspace():
        spacecounter = spacecounter+1
        end = i
        code_temp = code_temp + MORSE.get(code[(start):(end)])
        start = end+1
        
        print(code_temp)
    i=i+1
     
    
#add .capitlize() to capitalize string
