def generateBadMatchTab(pattern):
    badMList = {}
    for i in range(0, len(pattern)-1):
        badMList[pattern[i]] = len(pattern) - i - 1
    #badMList[pattern[i + 1]]=len(pattern)
    print badMList
    return badMList

def BoyMoore_algo(Text,pattern):
    n=len(Text)
    m=len(pattern)
    hits=[]
    i=0
    q=m
    badMTable=generateBadMatchTab(pattern)
    while((i+q-1)<n):
        while(pattern[q-1]==Text[i+q-1] and q>0):
            q=q-1
        if(q<=0):
            hits.append(i)
            i=i+1
        elif(pattern[q-1]!=Text[i+q-1]):
            if(badMTable.has_key(Text[i+q-1])):
                i=i+badMTable[Text[i+q-1]]
            else:
                i=i+m
        q=m
    return hits




Val= BoyMoore_algo("consistingasting","sting")
pattern="sting"
str="consistingasting"
print str
for j in Val:
    print str[j:j+len(pattern)]
print Val
