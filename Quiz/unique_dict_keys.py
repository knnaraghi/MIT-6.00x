##Test Cases

##aDict = { 0: 1, 1: 2, 2: 2, 4: 2, 5: 2, 6: 3, 7: 2}
##aDict = {'One': 1, 'Onee': 1, 'Two': 2, 'Three': 3}      
##aDict = {1: 1, 2: 2, 3: 3}
##aDict = {1: 1, 2: 1, 3: 1}
##aDict = {1: 1}
##aDict = {1: 1, 2: 1, 3: 3}  
##aDict = {2: 2, 3: 3, 4: 4}
##aDict = {}
##aDict = {2: 0, 3: 3, 6: 1}
##aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
##aDict = {0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0}
aDict = {8: 3, 1: 3, 2: 2}
##aDict = {2: 2, 5: 0, 7: 3}
##aDict = {5: 1, 7: 1}
##aDict = {5: 1, 7: 1}
##aDict = {0: 3, 1: 2, 2: 3, 3: 1, 4: 0, 6: 0, 7: 4, 8: 2, 9: 7, 10: 0}
##aDict = {0: 2, 1: 3, 2: 0, 3: 6, 7: 2, 9: 3}
##aDict = {8: 1, 0: 4, 1: 1, 5: 2, 9: 4}

def uniqueValues(aDict):
    
    valueslist = aDict.values()
    copy_valueslist = valueslist[:]
    keyslist = aDict.keys()
    uniquekeylist = []

    x=0

    for i in copy_valueslist:
        x += 1
        if i in copy_valueslist[x:]:
            while valueslist.count(i) >= 1:
                valueslist.remove(i)

    for e in valueslist:
        uniquekeylist.append(keyslist[copy_valueslist.index(e)])

    uniquekeylist.sort()

    return uniquekeylist
