count = 0
s = 'azcbobobegghakl'
for i in range(len(s)-2):
    if 'bob' in s[i:i+3]:
        count += 1
print ("Number of times Bob occurs is: " + str(count))
