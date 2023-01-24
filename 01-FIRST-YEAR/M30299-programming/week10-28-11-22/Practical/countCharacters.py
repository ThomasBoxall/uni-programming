def countCharacters():
    userString = input("Enter a string: ")
    countedDict = {}
    for currentChar in userString:
        if currentChar in countedDict:
            countedDict[currentChar] += 1
        else:
            countedDict[currentChar] = 1
    for dictCurrent in countedDict:
        print(str(countedDict[dictCurrent]) + " occurrences of "+ dictCurrent)
countCharacters()