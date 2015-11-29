pattern = "tooth"
text = "toothtrutoohsthardtothbrushtoothtoothes"
text = "abcdefgfhijlmnom"
text = "tiitottoothotttottotooth"
def get_bad_match_table(text):
    bad_match = {}
    length = len(text)
    i = length-1
    while i >=0:
        c = text[i]
        if not c in bad_match:
            bad_match[c]=i
        i = i-1
    return bad_match

def search_pattern(text,pattern):
    bad_match = get_bad_match_table(pattern)
    pattern_length = len(pattern)# n
    text_length = len(text) # m
    matches = []
    alignedAt = 0
    while (alignedAt + (pattern_length-1)) < text_length:
        indexInPattern = pattern_length-1
        while indexInPattern >=0:
            indexInText = alignedAt + indexInPattern
            x = text[indexInText]
            y = pattern[indexInPattern]
            if (indexInText >= text_length):
	        break;
            if x!=y:
                r = bad_match[x]
                if r == None:
                    alignedAt = indexInText + 1;
                else:
	            shift = indexInText - (alignedAt + r)
                    if shift > 0:
                        alignedAt += shift
                    else:
                        alignedAt + 1
            elif (indexInPattern == 0):
	        matches.add(alignedAt)
	        alignedAt+=1        
        indexInPattern = indexInPattern-1 
          
print text
print pattern
search_pattern(text,pattern)

