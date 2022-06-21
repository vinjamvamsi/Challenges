mydict = {"a":{"b":{"c":"d"}}}

keysinput = input()
SplitKeysintoList = keysinput.split("/")
tempdict = mydict

for i in range (0, len(SplitKeysintoList)):
    #print(mydict[x[i]])
    #print(x[i])
    tempdict = tempdict[SplitKeysintoList[i]]
    
result = tempdict
print(result)
