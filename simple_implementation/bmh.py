def BoyerMooreHorspool(pattern, text):
    m = len(pattern)
    n = len(text)
    k = 256
    skip = [m]*k
    # initialise the considering all the ascii 256
    #for k in range(256): skip.append(m)
    print skip
    print len(skip)
    # loop until second last letter initailise with length of pattern
    for letter in pattern[0:m-2]:
        ascii_val = ord(letter)
        skip[ascii_val]= m - k - 1
    print skip
    k = m - 1
    while k < n:
        j = m - 1; i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1; i -= 1
        if j == -1: return i + 1
        k += skip[ord(text[k])]
    return -1

if __name__ == '__main__':
    text = "thhethethethethe"
    pattern = "the"
    s = BoyerMooreHorspool(pattern, text)
    print 'Text:',text
    print 'Pattern:',pattern
    print s
    if s > -1:
        print 'Pattern \"' + pattern + '\" found at position',s

