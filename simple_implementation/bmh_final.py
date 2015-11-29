def bad_chars(pattern):
    m = len(pattern)
    badchars = {}
    for i in range(0,m-1):
        badchars[pattern[i]]= m-i-1
    return badchars

def suffixes(pattern,suffixes):
    m = len(pattern)
    suffixes[m-1]=m
    g = m-1
    
