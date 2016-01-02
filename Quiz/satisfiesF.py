def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """    
    L_Copy = L[:]
    for e in L_Copy:
        if f(e) != True:
            L.remove(e)
    return len(L)

def f(s):
    return 'a' in s
    
##Test Cases
##L = ['a', 'b', 'a']
##L = ['a', 'a', 'a']
##L = ['a', 'a', 'a', 'a', 'a', 'a']
##L = ['a', 'a', 'c', 'b', 'a', 'a']
L = ['a', 'a', 'c', 'b', 'd', 'a', 'a', 'a', 'c', 'b', 'd', 'j']
#print satisfiesF(L)
#print L


run_satisfiesF(L, satisfiesF)
