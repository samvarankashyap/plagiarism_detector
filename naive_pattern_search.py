txt = "AABAACAADAABAAABAA"
pat = "AABA"

def naive_search(text , pattern):
     len_of_text = len(text)
     len_of_pattern = len(pattern)
     for i in range(0,len_of_text):
         #print i
         #print text[i:i+len_of_pattern]
         #print pattern
         if  text[i:i+len_of_pattern] == pattern:
             print "pattern found at index" + str(i)
"""
def search(pat, txt):
    M = len(pat)
    N = len(txt)
 
    # A loop to slide pat[] one by one
    for i in xrange(N-M+1):
 
        # For current index i, check for pattern match
        for j in xrange(M):
            if txt[i+j] != pat[j]:
                break
        if j == M-1: # if pat[0...M-1] = txt[i, i+1, ...i+M-1]
            print "Pattern found at index " + str(i)
 
"""
import time
start_time = time.time()
naive_search(txt,pat)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
#search(txt,pat)
print("--- %s seconds ---" % (time.time() - start_time))

