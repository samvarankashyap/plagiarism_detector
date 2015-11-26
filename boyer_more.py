pattern = "tooth"
text = "toothtrutoohsthardtothbrushtoohtoothes"
text = "abcdefgfhijlmnom"
text = "tiitottoootttottotooth"
def get_bad_match_table(text):
    bad_match = {}
    length = len(text)
    for i in range(0,length):
        print i
        bad_match[text[i]] = length-i-1
    # * should be the length of string 
    bad_match["*"] = length
    # last letter should be length of the string
    print length 
    bad_match[text[length-1]]=length
    print bad_match
    return bad_match

def get_match(bad_match,letter):
    if letter in bad_match:
        return bad_match[letter]
    else:
        return bad_match["*"]

def search_pattern(text,pattern):
    bad_match = get_bad_match_table(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    pattern_end = pattern_length -1 
    i = pattern_end
    k = i
    match_counter =0
    while i < text_length:
        if text[i]!= pattern[k]:
            #i = i+ bad_match[text[i]]
            i = i + get_match(bad_match,text[i])
            k = pattern_end
            match_counter = 0
            continue
        if text[i] == pattern[k]:
            k = k-1
            i = i-1
            match_counter +=1
        if match_counter == pattern_length:
            print "pattern found at"
            print i+1
            break
print text
print pattern
search_pattern(text,pattern)

