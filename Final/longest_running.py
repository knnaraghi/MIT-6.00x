###TEST CONDITIONS###

#L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
#L = [0]
#L = [1, 1, 1, 1, 1]
#L = [-10, -5, 0, 5, 10]
#L = [-1, -2, -3, -4, -5, -6, -7, 2, 3]
#L = [1, 3, 5, -1, -3, -5, -7, 1, 3, 5]
#L = [10, 8, 9, 5, 6, 7, 1, 2, 3, 4]

def longestRun(L):
    """function to find longest running list of integers within a list"""
    #set longest running list to only include element of list
    longest_running = [L[0]]
    #create a working list 
    working_list = [L[0]]
    for i in range(len(L)-1):
        #check to see if subsequent element is greater than or equal
        if L[i+1] >= L[i]:
            #add to working list if so 
            working_list.append(L[i+1])
            #then check if working list is longer than longest running and change if so 
            if len(working_list) >= len(longest_running):
                longest_running = working_list
        #starts working list from next element if otherwise
        else:
            working_list = [L[i+1]]   
    return len(longest_running)

##Test
##longestRun(L)
