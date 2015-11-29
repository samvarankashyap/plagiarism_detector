import string_algos
from string_algos import BoyerMore
text ="AGTAfsdfsdfssdsasaaddas sadhnajddas"
pattern = "das"
 
l = BoyerMore.BoyerMore(text,pattern)
print l.search_pattern()
