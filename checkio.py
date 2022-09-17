checkio = [1,2,3,3,2,2,4,3,2,5]
print(checkio)
var = int(len(checkio))
while var > 0:
    var = var -1
    countvar = checkio[var]
    if checkio.count(countvar) == 1:
        checkio.remove(countvar)
        pass
print(checkio)


