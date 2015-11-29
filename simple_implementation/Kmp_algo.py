def generatePrefixTable(pattern):
    pstring=pattern
    i=0
    pref ={}
    pref[1]=0
    for j in range(2,len(pstring)):
        while(i>0 and pstring[i+1] != pstring[j]):
            i=pref[i]
        if pstring[i+1] == pstring[j]:
            i=i+1
        pref[j]=i
    return pref

def KMP_Algo(pattern,Text):
    n=len(Text)
    m=len(pattern)
    sText=" "+Text
    spattern=" "+pattern
    prefixTable= generatePrefixTable(spattern)
    q=0
    hits =[]
    for i in range(1,n+1):
        while(q>0 and spattern[q+1] != sText[i]):
            q = prefixTable[q]
        if(spattern[q+1]==sText[i]):
            q=q+1
        if(q==m):
            hits.append(str(i-m))
            q=prefixTable[q]
    return hits
def plagiot(userFile,allfiles,sAlgo):
    inp_file=open(userFile)
    read_file= inp_file.read()
    pattern=read_file.split("\n")
    for pattern_string in pattern:
        for file in allfiles:
            if pattern_string== "":
                continue
            main_file= open(file)
            Text=main_file.read()
            ans = {1 : KMP_Algo(pattern_string,Text), 2 : "is b"}[sAlgo]
            print ans
    pattern="acaacab"
    Text = "acbacaacaacacaacabcacaacab"

userFile="pattern.txt"
allfiles=["12-Days-to-Xmas.txt"]
option =1
plagiot(userFile,allfiles,option)
