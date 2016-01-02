def primesList(N):
    '''
    N: an integer
    '''
    primesList = []
    for i in range(2, N + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primesList.append(i)
    return primesList
