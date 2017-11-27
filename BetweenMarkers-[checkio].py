def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    
  
    varstart = text.find(begin)

    varend = text.find(end)

    varendlen = len(end)
    varlen = len(text)

    if text.find(begin) == -1:
        varstart = -1
    elif len(begin) > 1:
        varstart = (text.find(begin)+len(begin)-1)
    else:
        varstart = text.find(begin)

    if text.find(end) == -1:
        varend = -1
    

    if varstart < varend:
        text = text[(varstart+1):(varend)]
    elif varstart == -1 and varend == -1:
        text = text
    elif varstart == -1:
        text = text[0:(varend)]
    elif varend == -1:
        text = text[(varstart+1):varlen]
    elif varstart > varend:
        text = ""
    else:
        text = None
      
    return text
