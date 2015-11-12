import sys
def main():
    X ="AGGTAB"
    Y = "GXTXAYB"
    m = len(X)
    n = len(Y)
    print lcs(X,Y)

def lcs(X,Y):
    m = len(X)
    n = len(Y)
    counter = [[0]*(n+1) for x in range(m+1)]
    #printMatrix(counter)
    l = [[0]*(n+1) for i in range(m+1)]
    #printMatrix(l)
    print_matrix(l,m,n)
    for i in range(0,m+1):
        for j in range(0,n+1):
            if i==0 or j == 0:
                l[i][j] = 0
            elif X[i-1] == Y[j-1]:
                l[i][j] = l[i-1][j-1] +1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
    print_matrix(l,m,n)
    index = l[m][n]
    lcs= ['0']*index
    i = m 
    j = n
    while(i >0 and j>0):
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i= i-1
            j = j-1
            index = index-1
        elif l[i-1][j] > l[i][j-1]:
            i = i-1
        else:
            j = j-1
    return "".join(lcs)


def print_matrix(m,r,c):
    for i in range(0,r):
        sys.stdout.write("\n")
        for j in range(0,c):
            sys.stdout.write(str(m[i][j]))
            sys.stdout.write('\t')

    sys.stdout.write('\n')



main()
