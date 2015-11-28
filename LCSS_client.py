import string_algos
from string_algos import LCSS
text ="AGGTAB"
pattern = "GXTXAYB"
 
l = LCSS.LCSS(text,pattern)
print l.search_pattern()
