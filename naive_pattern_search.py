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


import time
start_time = time.time()
naive_search(txt,pat)
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
#search(txt,pat)
print("--- %s seconds ---" % (time.time() - start_time))

