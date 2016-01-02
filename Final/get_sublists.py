##Test Cases
##L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] ##test n = 4
##L = [1, 1, 1, 1, 4] ##test n = 2

def getSublists(L, n):
    '''prints out sublists of the list L which are each of length n'''
    ## initialize an empty list which will take in all sublists
    sublists = []
    ##for loop that loops over list L but does not go too far though subtracting the length n
    for i in range(len(L)-n+1):
        #create each sublist 
        subset = L[i:i+n]
        ##print subset - this was used for testing
        ##append the sublist to the list of sublists
        sublists.append(subset)
    return sublists

#Test
#getSublists(L, 4)
