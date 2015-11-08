
def lcs(X,Y,m,n):
   if m == 0 or n == 0:
     return 0
   if X[m-1] == Y[n-1]:
     return 1 + lcs(X, Y, m-1, n-1)
   else:
     return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
 
def max( a, b):
    if a > b:
        return a
    else:
        return b
 
def main():
  X = "AGGTAB"
  Y = "GXTXAYB"
 
  m = len(X)
  n = len(Y)
 
  print "Length of LCS is ", lcs( X, Y, m, n)

main()
