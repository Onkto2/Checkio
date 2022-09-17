def recallpassword(cipher_grille, ciphered_password):
#step2 - turn ciphered password into matrix
    listlenpw = len(ciphered_password)
    matrixpw = []
    matrixpwrow = []
    rowcountpw = 0
    while (rowcountpw < listlenpw):
        rowpw = ciphered_password[rowcountpw]
        placecountpw = 0
        testlistpw = []
        while (placecountpw < listlenpw):
            placepw = rowpw[placecountpw]
            testlistpw.append(placepw)
            matrixrowpw = testlistpw
            placecountpw = placecountpw + 1
        rowcountpw = rowcountpw +1
        matrixpw.append(matrixrowpw)
    #print(matrixpw)
​    password = ""
    password0 = ""
    password90 = ""
    password180 = ""
    password270 = ""
​​
    matrix = []
    matrix90 = []
    matrix180 = []
    matrix270 = []
    listlen = len(cipher_grille)
    matrixrow =[]
    rowcount =0
    while (rowcount < listlen):
        row =  cipher_grille[rowcount]
        placecount = 0
        testlist = []
        while(placecount < listlen):
            place = row[placecount]
            if place == 'X':
                testlist.append(1)
            if place == ".":
                testlist.append(0)
            placecount = placecount +1
            matrixrow = testlist
        rowcount = rowcount + 1
        matrix.append(matrixrow)
    print(matrix)
​
    locationarray = []
    rowcountar = 0
    columncountar = 0
    testlistar = []
    while (columncountar < listlen):
        while (rowcountar < listlen):
            if matrix[columncountar][rowcountar] == 1:
                #print("success!")
                testlist = []
                testlist.append(columncountar)
                testlist.append(rowcountar)
                testlistar = testlist
                locationarray.append(testlistar)
            rowcountar = rowcountar + 1
        columncountar = columncountar + 1
        rowcountar = 0
    #print(locationarray)
​
    searchposition = 0
    listlenAR = len(locationarray)
    while(searchposition < listlenAR):
        temp1 = locationarray[searchposition][0]
        temp2 = locationarray[searchposition][1]
        temp3 = matrixpw[temp1][temp2]
        password0+=str(temp3)
        searchposition = searchposition +1
        if(searchposition == listlenAR):
            print(password0)
​
    cipher90 = list(zip(*cipher_grille[::-1]))
    listlen = len(cipher90)
    matrixrow =[]
    rowcount =0
    while (rowcount < listlen):
        row =  cipher90[rowcount]
        placecount = 0
        testlist = []
        while(placecount < listlen):
            place = row[placecount]
            if place == 'X':
                testlist.append(1)
            if place == ".":
                testlist.append(0)
            placecount = placecount +1
            matrixrow = testlist
        rowcount = rowcount + 1
        matrix90.append(matrixrow)
    print(matrix90)
​
    locationarray = []
    rowcountar = 0
    columncountar = 0
    testlistar = []
    while (columncountar < listlen):
        while (rowcountar < listlen):
            if matrix90[columncountar][rowcountar] == 1:
                #print("success!")
                testlist = []
                testlist.append(columncountar)
                testlist.append(rowcountar)
                testlistar = testlist
                locationarray.append(testlistar)
            rowcountar = rowcountar + 1
        columncountar = columncountar + 1
        rowcountar = 0
    #print(locationarray)
​
    searchposition = 0
    listlenAR = len(locationarray)
    while(searchposition < listlenAR):
        temp1 = locationarray[searchposition][0]
        temp2 = locationarray[searchposition][1]
        temp3 = matrixpw[temp1][temp2]
        password90+=str(temp3)
        searchposition = searchposition +1
        if(searchposition == listlenAR):
            print(password90)
​
​
​
    cipher180 = list(zip(*cipher90[::-1]))
    listlen = len(cipher180)
    matrixrow =[]
    rowcount =0
    while (rowcount < listlen):
        row =  cipher180[rowcount]
        placecount = 0
        testlist = []
        while(placecount < listlen):
            place = row[placecount]
            if place == 'X':
                testlist.append(1)
            if place == ".":
                testlist.append(0)
            placecount = placecount +1
            matrixrow = testlist
        rowcount = rowcount + 1
        matrix180.append(matrixrow)
    print(matrix180)
​
    locationarray = []
    rowcountar = 0
    columncountar = 0
    testlistar = []
    while (columncountar < listlen):
        while (rowcountar < listlen):
            if matrix180[columncountar][rowcountar] == 1:
                #print("success!")
                testlist = []
                testlist.append(columncountar)
                testlist.append(rowcountar)
                testlistar = testlist
                locationarray.append(testlistar)
            rowcountar = rowcountar + 1
        columncountar = columncountar + 1
        rowcountar = 0
    #print(locationarray)
​
    searchposition = 0
    listlenAR = len(locationarray)
    while(searchposition < listlenAR):
        temp1 = locationarray[searchposition][0]
        temp2 = locationarray[searchposition][1]
        temp3 = matrixpw[temp1][temp2]
        password180+=str(temp3)
        searchposition = searchposition +1
        if(searchposition == listlenAR):
            print(password180)
​
    cipher270 = list(zip(*cipher180[::-1]))
    listlen = len(cipher270)
    matrixrow =[]
    rowcount =0
    while (rowcount < listlen):
        row =  cipher270[rowcount]
        placecount = 0
        testlist = []
        while(placecount < listlen):
            place = row[placecount]
            if place == 'X':
                testlist.append(1)
            if place == ".":
                testlist.append(0)
            placecount = placecount +1
            matrixrow = testlist
        rowcount = rowcount + 1
        matrix270.append(matrixrow)
    print(matrix270)
​
    locationarray = []
    rowcountar = 0
    columncountar = 0
    testlistar = []
    while (columncountar < listlen):
        while (rowcountar < listlen):
            if matrix270[columncountar][rowcountar] == 1:
                #print("success!")
                testlist = []
                testlist.append(columncountar)
                testlist.append(rowcountar)
                testlistar = testlist
                locationarray.append(testlistar)
            rowcountar = rowcountar + 1
        columncountar = columncountar + 1
        rowcountar = 0
    #print(locationarray)
​
    searchposition = 0
    listlenAR = len(locationarray)
    while(searchposition < listlenAR):
        temp1 = locationarray[searchposition][0]
        temp2 = locationarray[searchposition][1]
        temp3 = matrixpw[temp1][temp2]
        password270+=str(temp3)
        searchposition = searchposition +1
        if(searchposition == listlenAR):
            print(password270)
​
    password+=str(password0)+str(password90)+str(password180)+str(password270)
    print(password)
​
    return password
​
