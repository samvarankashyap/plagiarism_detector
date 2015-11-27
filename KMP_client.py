import string_algos
from string_algos import KMP
text ="AGTAdasdasdasdadBdsadasdsadasdasdssadad"
pattern = "das"
 
l = KMP.KMP(text,pattern)
print l.search_pattern()
