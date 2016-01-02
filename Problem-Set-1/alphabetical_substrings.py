s = 'azcbobobegghakl'
temp = s[0] #holding place for string
alphabetical = s[0] #will hold alphabetical substring
for i in range(1, len(s)): 
    if s[i] >= temp[-1:]: #alphabetical comparison
        temp = temp + s[i]
        if len(temp) > len(alphabetical): 
            alphabetical = temp
    else:
        temp = s[i]
print ("Longest substring in alphabetical order is: " + alphabetical)
